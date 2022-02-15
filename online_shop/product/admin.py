from django.contrib import admin
from product.models import Category, Discount, OffCode, Brand, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(OffCode)
admin.site.register(Brand)
admin.site.register(Product)
