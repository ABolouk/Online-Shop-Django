from django.urls import path
from customer import views

# app_name = "customer"
urlpatterns = [
    # path("order_history/", views.OrderHistoryView.as_view(), name="order-history"),
    # path("order_status/", views.OrderStatusView.as_view(), name="order-status"),
    path("address/", views.AddressView.as_view(), name="address"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile-update"),
]
