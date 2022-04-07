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
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            try:
                order = customer.order_set.get(is_open=True)
                order_item = OrderItem.objects.create(order=order, product=Product.objects.get(id=product_id), number=number)
            except:
                pass
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


class GetCart(APIView):
    def get(self, request):
        data = request.session.get("cart", None)
        return Response(data=data)


class DeleteFromCart(APIView):
    def get(self, request):
        product_id = request.query_params['product_id']
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            try:
                order = customer.order_set.get(is_open=True)
                product = Product.objects.get(id=product_id)
                order_item = order.orderitem_set.filter(product=product).first()
                order_item.delete()
            except:
                pass
        data = request.session["cart"]
        request.session.pop("cart")
        data.pop(product_id)
        request.session["cart"] = data
        return Response({"msg": _("Product deleted from cart.")})
