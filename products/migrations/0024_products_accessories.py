# Generated by Django 2.0.5 on 2018-11-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='accessories',
            field=models.BooleanField(default=False),
        ),
    ]
