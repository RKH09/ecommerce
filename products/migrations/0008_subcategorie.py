# Generated by Django 2.0.5 on 2018-10-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]