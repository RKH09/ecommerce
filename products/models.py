import random
import os
from django.db import models

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

class Products(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  
  
    def __str__(self):
        return self.title
