from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse

from django.views import View
from customer.models import Customer


class ProfileView(PermissionRequiredMixin, View):
    permission_required = ["being_customer", ]

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        user = request.user
        print(user)
        print(user.id)
        customer = Customer.objects.get(user_id=user.id)
        context = {
            "customer": customer,
        }
        return render(request=request, template_name="customer/customer_profile.html", context=context)
