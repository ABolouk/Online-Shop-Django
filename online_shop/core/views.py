from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.views import View
from customer.models import Customer
from core.models import User
from customer.forms import UserForm
from core.forms import LoginForm


class CustomerRegisterView(View):
    def get(self, request):
        form = UserForm()
        context = {
            "form": form,
        }
        return render(request=request, template_name="core/customer_register.html",
                      context=context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user: User = User.objects.create_user(phone=phone, password=password)
            customer = Customer.objects.create(user=user)
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect("customer:profile")
        else:
            context = {
                "form": form,
            }
            return render(request=request, template_name="core/customer_register.html", context=context)


class CustomerLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("customer:profile")
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request=request, template_name="core/login_customer.html", context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect("customer:profile")
            else:
                messages.error(request, _("Phone or password is incorrect."), "danger")
                return redirect("login-customer")

        context = {
            "form": form,
        }
        return render(request=request, template_name="core/login_customer.html", context=context)


def logout_view(request):
    if request.method == "GET":
        logout(request)
        messages.success(request, _("User logged out successfully."), "success")
        return HttpResponseRedirect(reverse("login-customer"))
