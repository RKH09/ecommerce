# Generated by Django 2.0.5 on 2018-11-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email_id',
            field=models.EmailField(max_length=150, null=True),
        ),
    ]