"""blushbyanshii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from .import views 
from products import views
from django.urls import path
from carts.views import cart_home
from accounts.views import my_profile
from .views import home_page,contact_page, login_page, signup,logout_user
from products.views import product_list, product_featured_list, search_list, tag_list,category_list


app_name = 'products'

app_name = 'shopping_cart'


urlpatterns = [
    path('',home_page),
    path('admin/', admin.site.urls),
    path('', include('shopping_cart.urls', namespace='shopping_cart')),
    path('contact/',contact_page),
    path('login/',login_page),
    path('signup/',signup),
    path('logout/', logout_user, name='logout_user'),
    path('', include('products.urls', namespace='products')),
    path('products/', product_list, name='product-list'),
    path('search/', search_list, name="query"),
    path('tags/', tag_list, name="tags"),
    path('category/', category_list, name="category"),
    path('profile/', my_profile, name="profile"),
    path('lookbook/', product_featured_list, name='lookbook'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^products/(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    path('cart/', cart_home, name='cart')
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)