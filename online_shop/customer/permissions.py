from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser
from rest_framework.request import Request


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer.user


class IsSuperuserPermission(IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser


# class IsSuperuserPermission(IsAdminUser):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)
