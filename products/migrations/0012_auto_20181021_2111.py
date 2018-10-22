# Generated by Django 2.0.5 on 2018-10-21 21:11

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20181021_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]