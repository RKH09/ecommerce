from django.conf import settings
from django.db import models

from products.models import Products

User = settings.AUTH_USER_MODEL

class Carts(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    products    = models.ManyToManyField(Products, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
