# Generated by Django 3.2.6 on 2021-08-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='ویژه'),
        ),
    ]
