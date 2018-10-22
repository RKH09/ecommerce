from django.conf.urls import url
from django.urls import path
from .views import product_list, search_list, search_list

app_name = 'products'

urlpatterns = [
    path('products/', product_list, name='product-list'),
]
