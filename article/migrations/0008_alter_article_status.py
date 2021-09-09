# Generated by Django 3.2.6 on 2021-08-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210823_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'رد شده')], default='d', max_length=1, verbose_name='وضعیت'),
        ),
    ]