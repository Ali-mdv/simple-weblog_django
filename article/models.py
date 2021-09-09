from django.db import models
from django.utils import timezone
from extentions.converter import convert_to_jalali
from django.utils.html import format_html
from user.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating

from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator

# Create your models here.

# Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی')

    def __str__(self):
        return self.ip_address


class Category(models.Model):
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.CASCADE,related_name='children',verbose_name='عبارات زیر دسته')
    title = models.CharField(max_length=100,verbose_name='دسته بندی')
    slug = models.SlugField(max_length=100,verbose_name='آدرس')
    status = models.BooleanField(default=True,verbose_name='آیا نمایش داده شود')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOISE = (
        ('d','پیش نویس'),
        ('p','منتشر شده'),
        ('i','در حال بررسی'),
        ('b','رد شده'),
    )

    author = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name='articles',verbose_name='نویسنده')
    title = models.CharField(max_length=200,verbose_name='عنوان')
    slug =  models.SlugField(max_length=100,unique=True,verbose_name='آدرس')
    category = models.ManyToManyField(Category,related_name='articles',verbose_name='دسته بندی')
    describtion = models.TextField(verbose_name='توضیحات')
    picture = models.ImageField(upload_to='image',verbose_name='عکس')
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True,verbose_name='فیلم',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    publish = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
    status = models.CharField(default='d',max_length=1,choices=STATUS_CHOISE,verbose_name='وضعیت')
    is_special = models.BooleanField(default=False,verbose_name='ویژه')
    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating)
    hits = models.ManyToManyField(IpAddress,blank=True,related_name='hits',through='ArticleHits',verbose_name='بازدید ها')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return convert_to_jalali(self.publish)
    jpublish.short_description = 'تاریخ انتشار'

    def category_to_str(self):
        return ', '.join([category.title for category in self.category.active()])
    category_to_str.short_description = 'دسته بتدی'

    def picture_tag(self):
        return format_html('<img src="{}" width=80px height=50px>'.format(self.picture.url))
    picture_tag.short_description = 'عکس'


    def get_absolute_url(self):
        return reverse('account:home')

    def hits_count(self):
        return self.hits.count()
    hits_count.short_description = 'بازدید'


    def safe_descibtion(self):
        return mark_safe(self.describtion)


    objects = ArticleManager()


class ArticleHits(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
