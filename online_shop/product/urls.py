from django.urls import path
from .views import ProductListAPI, ProductDetailAPI

urlpatterns = [
    path("list_api/", ProductListAPI.as_view(), name="product_list_api"),
    path("api/<int:pk>", ProductDetailAPI.as_view(), name="product_detail_api"),
]
