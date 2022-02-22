from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from customer.models import Customer
from core.models import User
from customer.forms import CustomerRegisterForm, UserForm


class CustomerRegister(View):
    def get(self, request):
        form = UserForm()
        context = {
            "form": form,
        }
        return render(request=request, template_name="customer/customer_register.html", context=context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user: User = User.objects.create_user(phone=phone, password=password)
            customer = Customer.objects.create(user=user)
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return HttpResponse(f"{customer}")
        else:
            context = {
                "form": form,
            }
            return render(request=request, template_name="customer/customer_register.html", context=context)


class CustomerLogin(View):
    pass
