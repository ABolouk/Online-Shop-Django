from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.

# def product_list_view(request):
#     if request.method == "POST":
#         data = request.POST
#         product_deserializer = ProductSerializer(data=data)
#         if product_deserializer.is_available():
#             new_product = product_deserializer.save()
#             return JsonResponse({'new_car_id': new_product.id}, status=201)
#         else:
#             JsonResponse({"errors": product_deserializer.errors}, status=400)
#
#     elif request.method == "GET":
#         product_serializer = ProductSerializer(instance=Product.objects.all(), many=True)
#         print(product_serializer.data)
#         return JsonResponse({"data": product_serializer.data}, status=200)
#
#     else:
#         return JsonResponse({"msg": "invalid method!"}, status=405)

class ProductListAPI(APIView):
    def get(self, request):
        product_serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(product_serializer.data, status=200)

    def post(self, request):
        product_serializer = ProductSerializer(data=request.POST)
        if product_serializer.is_valid():
            new_product = product_serializer.save()
            return Response({'new_product_id': new_product.id}, status=201)
        else:
            return Response({'errors': product_serializer.errors}, status=400)


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
