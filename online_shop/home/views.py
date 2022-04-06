from django.views import View
from django.shortcuts import render

from product.models import Product, Category


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.parents()
        context = {
            "products": products,
            "categories": categories,
        }
        return render(request, template_name="product/home.html", context=context)
