from django.views import View
from django.shortcuts import render

from product.models import Product


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            "products": products
        }
        return render(request, template_name="product/home.html", context=context)