# Generated by Django 2.0.5 on 2018-10-21 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_tags_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='slug',
        ),
    ]
