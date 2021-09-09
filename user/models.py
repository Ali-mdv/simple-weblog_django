from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True,verbose_name='ایمیل')
    is_author = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    special_user = models.DateTimeField(default=timezone.now,verbose_name='کاربر ویژه تا')
    profile_photo = models.ImageField(upload_to='profiles',verbose_name='عکس', default='default-profile.png',null=True, blank=True)
    about_author = models.TextField(max_length=200,verbose_name='درباره نویسنده',default='سلام')

    facebook_id = models.SlugField(unique=True,max_length=50,verbose_name='آدرس اکانت فیسبوک',blank=True)
    youtube_id = models.SlugField(unique=True,max_length=50,verbose_name='آدرس اکانت یوتیوب',blank=True)
    twitter_id = models.SlugField(unique=True,max_length=50,verbose_name='آدرس اکانت توییتر',blank=True)
    instagram_id = models.SlugField(unique=True,max_length=50,verbose_name='آدرس اکانت اینستاگرام',blank=True)

    def is_special(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special.boolean = True
    is_special.short_description = 'وضعیت کاربری ویژه'

    # def get_absolute_url(self):
    #     return reverse('account:profile')