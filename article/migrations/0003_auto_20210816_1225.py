# Generated by Django 3.2.6 on 2021-08-16 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_rename_published_article_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='دسته بندی')),
                ('slug', models.SlugField(max_length=100, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='article',
            name='describtion',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='image', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='آدری'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضیعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='article.Category', verbose_name='دسته بندی'),
        ),
    ]