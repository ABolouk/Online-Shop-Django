from django.contrib import admin
from order.models import OrderItem, Order


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'order')
    search_fields = ('product',)
    list_filter = ('order',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'is_open', 'is_paid')
    search_fields = ('customer', 'address')
    list_filter = ('off_code', 'is_paid')


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
