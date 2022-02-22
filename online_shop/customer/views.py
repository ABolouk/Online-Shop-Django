from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse

from django.views import View
from django.views.generic import UpdateView, ListView, DetailView

from core.models import User
from customer.models import Customer, Address
from customer.forms import ProfileForm
from order.models import Order


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


class ProfileUpdateView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        user = request.user
        customer = user.customer
        data = {
            "first_name": user.last_name,
            "last_name": user.first_name,
            "phone": user.phone,
            "password": user.password,
        }
        form = ProfileForm(data=data)
        context = {
            "form": form,
        }
        return render(request=request, template_name="customer/customer_update.html", context=context)

    def post(self, request):
        user = request.user
        data = request.POST
        user.phone = data['phone']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.password = data['password']
        user.save()
        return HttpResponseRedirect(reverse("profile"))


class OrderHistoryView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        user = request.user
        customer = user.customer
        orders = Order.objects.filter(customer=customer)
        context = {
            "orders": orders,
        }
        return render(request=request, template_name="customer/customer_order_history.html", context=context)


class OrderHistoryListView(PermissionRequiredMixin, DetailView):
    permission_required = "customer.being_customer"
    model = Order
    template_name = "customer/order_items.html"
