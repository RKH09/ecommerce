from django.contrib import admin
from .models import contact_form
from carts.models import Carts
from accounts.models import Profile
# Register your models here.


admin.site.register(Carts)
admin.site.register(Profile)
admin.site.register(contact_form)