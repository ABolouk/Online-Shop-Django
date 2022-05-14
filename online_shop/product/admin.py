from django.contrib import admin
from product.models import Category, Discount, OffCode, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_parent')
    list_filter = ('is_parent',)
    search_fields = ('name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class OffCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'is_available', 'category')
    search_fields = ('name',)
    list_filter = ('brand', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(OffCode, OffCodeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
