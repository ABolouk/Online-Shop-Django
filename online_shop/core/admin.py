from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User

UserAdmin.fieldsets[0][1]['fields'] = ('phone', 'password')
UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.list_display = ('phone', 'first_name', 'last_name', 'email')
UserAdmin.ordering = ('phone',)

admin.site.register(User, UserAdmin)
