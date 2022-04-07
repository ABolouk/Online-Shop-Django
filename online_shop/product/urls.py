from django.urls import path
from . import api_views
from . import views

app_name = "product"
urlpatterns = [
    path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path('category/<int:category_id>/', views.CategoryProductView.as_view(), name="category"),
    path('brand/<int:brand_id>/', views.BrandProductView.as_view(), name="brand"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('api/list/', api_views.ProductListAPI.as_view(), name="list_api"),
    # path("list_api/", views.ProductListAPI.as_view(), name="product_list_api"),
    # path("api/<int:pk>", views.ProductDetailAPI.as_view(), name="product_detail_api"),
]
