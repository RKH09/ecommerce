# Generated by Django 2.0.5 on 2018-10-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_subcategorie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategorie',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
