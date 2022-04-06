from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.generic import DetailView
from django.views import View

from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics

from product.models import Product, Category, Brand
from product.serializers import ProductSerializer


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


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail_view.html"


class CategoryProductView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        if category.is_parent:
            products = category.children_products()
        else:
            products = category.product_set.all()
        categories = Category.parents()
        brands = Brand.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "brands": brands,
        }
        return render(request=request, template_name="product/home.html", context=context)


class BrandProductView(View):
    def get(self, request, brand_id):
        brand = Brand.objects.get(id=brand_id)
        products = brand.product_set.all()
        categories = Category.parents()
        brands = Brand.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "brands": brands,
        }
        return render(request=request, template_name="product/home.html", context=context)

