import random
import os
import uuid
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,99999999990)
    name, ext = get_filename_ext(filename)
    finalname = f'{new_filename}{ext}'
    return "products/{finalname}".format(finalname=finalname)


class Category(models.Model):
        title   = models.CharField(max_length=100)

        def __str__(self):
                return self.title

class SubCategorie(models.Model):
        title       = models.CharField(max_length=100)
        category    = models.ManyToManyField(Category)

        def __str__(self):
                return self.title


class Tags(models.Model):
        name    = models.CharField(max_length=100)
        def __str__(self):
                return self.name


class Products(models.Model): 
    title       = models.CharField(max_length=150)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image1       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    category    = models.ManyToManyField(SubCategorie)
    tags        = models.ManyToManyField(Tags)
    featured    = models.BooleanField(default = False)
    
  
    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender = Products)

