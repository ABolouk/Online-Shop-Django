from django.views import View
from django.shortcuts import render

from product.models import Product, Category, Brand


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.parents()
        brands = Brand.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "brands": brands,
        }
        return render(request, template_name="product/home.html", context=context)
