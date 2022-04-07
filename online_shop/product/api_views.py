from rest_framework.response import Response
from rest_framework import generics, authentication
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _

from .models import Product
from order.models import OrderItem, Order
from .serializers import ProductSerializer


class ProductListAPI(generics.ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    authentication = [authentication.BasicAuthentication]
    # permissions = [IsSuperuserPermission]


class AddToCart(APIView):
    authentication = [authentication.BasicAuthentication]

    def get(self, request):
        product_id = request.query_params.get("product_id")
        number = request.query_params.get("number")
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(instance=product)
        try:
            data = request.session["cart"]
            data.update({product_id: {"number": number, "name": Product.objects.get(id=product_id).name}})
            request.session.pop("cart")
            request.session["cart"] = data
        except:
            request.session["cart"] = {product_id: {"number": number, "name": Product.objects.get(id=product_id).name}}
        return Response(data=serializer.data)
