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
from django.conf.urls import url
from .import views
from products import views
from django.urls import path
from .views import home_page,contact_page, login_page, signup,logout_user
from products.views import product_list
app_name = 'products'

urlpatterns = [
    path('',home_page),
    path('admin/', admin.site.urls),
    path('contact/',contact_page),
    path('login/',login_page),
    path('signup/',signup),
    path('logout/', logout_user, name='logout_user'),
    path('products/', product_list),
    url(r'^products/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)