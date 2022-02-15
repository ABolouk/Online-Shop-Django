from datetime import date
from django.test import TestCase

from customer.models import Customer
from order.models import Order, OrderItem
from product.models import DiscountCode, Product, Discount, Category, Brand


class OrderItemTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(first_name="amir", last_name="bolouk", birth_date=date(1997, 5, 21))

        self.category = Category.objects.create(name="Electronics")

        self.brand = Brand.objects.create(name="ASUS")

        self.product = Product.objects.create(name="Zephyrus", brand=self.brand, price="56000000", detail="Blah Blah")
        self.product.category.add(self.category)
        # self.product2 = Product.objects.create(name="ZenPhone", brand=self.brand, price="6500000", detail="Halb")
        # self.product2.category.add(self.category)

        self.order = Order.objects.create(customer=self.customer)

        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, number=2)

    def test1_order_item_details(self):
        self.assertEqual("2", self.order_item.number)
        self.assertEqual("Zephyrus", self.order_item.product.name)
        self.assertEqual("112000000", self.order_item.price())
        self.assertEqual(self.order, self.order_item.order)
