# Generated by Django 3.2.6 on 2021-09-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20210907_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook_id',
            field=models.SlugField(blank=True, unique=True, verbose_name='آدرس اکانت فیسبوک'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram_id',
            field=models.SlugField(blank=True, unique=True, verbose_name='آدرس اکانت اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter_id',
            field=models.SlugField(blank=True, unique=True, verbose_name='آدرس اکانت توییتر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='youtube_id',
            field=models.SlugField(blank=True, unique=True, verbose_name='آدرس اکانت یوتیوب'),
        ),
    ]
