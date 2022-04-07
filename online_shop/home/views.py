from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from product.models import Product, Category, Brand
from order.models import Order, OrderItem


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


class CartView(PermissionRequiredMixin, View):
    permission_required = "customer.being_customer"

    def get(self, request):
        customer = request.user.customer
        addresses = customer.address_set.all()
        try:
            order = customer.order_set.get(is_open=True)
        except:
            order = Order.objects.create(customer=customer, address=customer.address_set.first())
            data: dict = request.session.get("cart", {})
            for product_id, data in data.items():
                number = data["number"]
                product = Product.objects.get(id=product_id)
                order_item = OrderItem.objects.create(order=order, product=product, number=number)
            order.save()

        products = Product.objects.all()
        categories = Category.parents()
        brands = Brand.objects.all()
        context = {
            "order": order,
            "addresses": addresses,
            "products": products,
            "categories": categories,
            "brands": brands,
        }
        return render(request, template_name="home/cart_home.html", context=context)
