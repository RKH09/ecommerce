# Generated by Django 2.0.5 on 2018-10-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181010_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
