# Generated by Django 2.0.5 on 2018-10-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_tags_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
