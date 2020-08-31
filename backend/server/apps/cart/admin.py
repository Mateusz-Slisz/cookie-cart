from django.contrib import admin

from server.apps.cart.models import Cart, Item

admin.site.register(Cart)
admin.site.register(Item)
