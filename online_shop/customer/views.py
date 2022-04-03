from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions, authentication

from django.views import View
from django.views.generic import UpdateView, ListView, DetailView, CreateView

from core.models import User
from customer.models import Customer, Address
from customer.forms import ProfileForm, ChangePasswordForm
from order.models import Order
from customer.serializers import AddressSerializer, UserSerializer
from customer.permissions import IsOwnerPermission, IsSuperuserPermission


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
        # customer = user.customer
        # data = {
        #     "first_name": user.last_name,
        #     "last_name": user.first_name,
        #     "phone": user.phone,
        #     # "password": user.password,
        # }
        # # form = ProfileForm(data=data)
        form = ProfileForm(instance=user)
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
        user.save()
        return HttpResponseRedirect(reverse("customer:profile"))


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


# class UserListView()
# class UserDetailView()

class AddressListView(generics.ListAPIView):
    model = Address
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permissions = [IsSuperuserPermission]
    authentication = [authentication.BasicAuthentication]


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permissions = [IsOwnerPermission]
    authentication_classes = [authentication.BasicAuthentication]


class PasswordChangeView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        form = ChangePasswordForm()
        context = {
            "form": form
        }
        return render(request=request, template_name="customer/change_password.html", context=context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            new_password = form.cleaned_data["new_password"]
            user.set_password(new_password)
            user.save()
            messages.success(request, _("Password successfully changed"), "success")
            return redirect("customer:profile")
        else:
            context = {
                "form": form
            }
            messages.error(request, _("Enter a valid password."), "danger")
            return render(request=request, template_name="customer/change_password.html", context=context)


class AddAddressView(PermissionRequiredMixin, CreateView):
    permission_required = "customer.being_customer"

    model = Address
    fields = ["province", "city", "detail"]
    template_name = "customer/add_address.html"
    success_url = reverse_lazy("customer:address")

    def form_valid(self, form):
        address = form.save(commit=False)
        customer = Customer.objects.get(user=self.request.user)
        address.customer = customer
        address.save()
        messages.success(self.request, _("Address successfully added."), "success")
        return super().form_valid(form)
