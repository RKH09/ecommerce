from django.contrib import admin
from .models import Products, Category, SubCategorie, Tags, Gallery, Subscription, bannerImage



# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Products

admin.site.register(Products, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategorie)
admin.site.register(Tags)
admin.site.register(Gallery)
admin.site.register(Subscription)
admin.site.register(bannerImage)