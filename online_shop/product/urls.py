from django.urls import path
from .views import product_list_view

urlpatterns = [
    path("list_view/", product_list_view)
]