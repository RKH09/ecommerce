from django.db import models

class contact_form(models.Model):
    fullname = models.CharField(max_length=100)
    email    = models.EmailField()
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)