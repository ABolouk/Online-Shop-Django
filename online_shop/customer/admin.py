from django.contrib import admin
from customer.models import Customer, Address


class CustomerAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'province', 'city', 'detail')
    list_filter = ('province', 'city')
    search_fields = ('province', 'city', 'detail')
    raw_id_fields = ('customer',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
