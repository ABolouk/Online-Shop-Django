from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.text import gettext_lazy as _

from .models import Order
from customer.models import Address


class AddressChange(APIView):
    def get(self, request):
        customer = request.user.customer
        order = customer.order_set.get(is_open=True)
        address_id = request.query_params['address_id']
        address = Address.objects.get(id=address_id)
        order.address = address
        order.save()
        return Response({"msg": _("Address successfully changed.")})
