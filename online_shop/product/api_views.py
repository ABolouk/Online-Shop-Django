from rest_framework import generics, authentication
from .models import Product
from .serializers import ProductSerializer


class ProductListAPI(generics.ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    authentication = [authentication.BasicAuthentication]
    # permissions = [IsSuperuserPermission]
