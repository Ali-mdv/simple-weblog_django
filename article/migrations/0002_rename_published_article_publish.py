# Generated by Django 3.2.6 on 2021-08-15 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish',
        ),
    ]
