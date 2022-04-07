from django.urls import path, include
from . import views

app_name = "order"
urlpatterns = [
    path("address_change/", views.AddressChange.as_view(), name="address_change"),
]
