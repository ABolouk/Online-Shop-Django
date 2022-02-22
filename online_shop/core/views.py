from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

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
            return HttpResponse(reverse("login"))
        else:
            context = {
                "form": form,
            }
            return render(request=request, template_name="core/customer_register.html", context=context)


class CustomerLoginView(View):
    def get(self, request):
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
            else:
                print("WHATTTT??")
                pass  # TODO: add a warning message

        context = {
            "form": form,
        }
        return render(request=request, template_name="core/login_customer.html", context=context)


def logout_view(request):
    logout(request)
    return HttpResponse(reverse("login-customer"))