from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse

from django.views import View
from customer.models import Customer, Address


class ProfileView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        if not request.user.is_authenticated:
            # TODO: add an error message
            return HttpResponseRedirect(reverse("login-customer"))
        user = request.user
        customer = Customer.objects.get(user_id=user.id)
        context = {
            "customer": customer,
        }
        return render(request=request, template_name="customer/customer_profile.html", context=context)


class AddressView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        customer = request.user.customer
        addresses = Address.objects.filter(customer=customer)
        context = {
            "addresses": addresses,
            "customer": customer,
        }
        return render(request=request, template_name="customer/customer_address.html", context=context)
