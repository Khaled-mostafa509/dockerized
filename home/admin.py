from django.contrib import admin
from .models import Product, Category, Recommended, Order, OrderItem, Cart, CartItem
# from modeltranslation.admin import TranslationAdmin


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Recommended)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
