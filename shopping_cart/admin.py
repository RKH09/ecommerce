from django.contrib import admin
from .models import OrderItem, Order, Transaction, Delivery, Wishlist, WishItem

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Wishlist)
admin.site.register(Delivery)
admin.site.register(WishItem)