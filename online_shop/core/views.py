from django.shortcuts import render

from django.views import View
from customer.models import Customer
from customer.forms import CustomerRegisterForm, UserForm


class CustomerRegister(View):
    def get(self, request):
        user_form = CustomerRegisterForm()
        customer_form = UserForm()
        context = {
            "user_form": user_form,
            "customer_form": customer_form,
        }
        return render(request=request, template_name="customer/customer_register.html", context=context)


class CustomerLogin(View):
    pass
