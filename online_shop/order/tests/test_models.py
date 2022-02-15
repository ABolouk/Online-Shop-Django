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

        self.order = Order.objects.create(customer=self.customer)

        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, number=2)

    def test1_order_item_number(self):
        self.assertEqual(2, self.order_item.number)

    def test2_order_item_product_name(self):
        self.assertEqual("Zephyrus", self.order_item.product.name)

    def test3_order_item_order(self):
        self.assertEqual(self.order, self.order_item.order)

    def test4_order_item_price(self):
        self.assertEqual("112000000", self.order_item.price())


class OrderTest(OrderItemTest):
    def setUp(self) -> None:
        super().setUp()
        self.product1 = self.product
        self.product2 = Product.objects.create(name="ZenPhone", brand=self.brand, price="6500000", detail="Halb")
        self.product2.category.add(self.category)
        self.product3 = Product.objects.create(name="Bad Bezn", brand=self.brand, price="1750000", detail="Halblah")

        self.discount_code1 = DiscountCode.objects.create(code="ABDC", type="VAL", amount="450000")
        self.discount_code2 = DiscountCode.objects.create(code="EFHG", type="PER", amount="50", max_value="1000000")

        self.order1 = Order.objects.create(customer=self.customer, discount_code=self.discount_code1)
        self.order2 = Order.objects.create(customer=self.customer, discount_code=self.discount_code2)
        self.order3 = Order.objects.create(customer=self.customer, discount_code=self.discount_code2)

        self.order_item1 = OrderItem.objects.create(order=self.order1, product=self.product1, number=1)
        self.order_item2 = OrderItem.objects.create(order=self.order1, product=self.product2, number=2)
        self.order_item3 = OrderItem.objects.create(order=self.order2, product=self.product2, number=1)
        self.order_item4 = OrderItem.objects.create(order=self.order3, product=self.product3, number=1)

    def tes5_order1_customer_fullname(self):
        self.assertEqual(self.customer.full_name(), self.order1.customer.full_name())

    def test6_customer_order_set(self):
        self.assertIn(self.order1, self.customer.order_set.all())
        self.assertIn(self.order2, self.customer.order_set.all())

    def test7_order1_order_item_set(self):
        self.assertIn(self.order_item1, self.order1.orderitem_set.all())
        self.assertIn(self.order_item2, self.order1.orderitem_set.all())

    def test8_order1_price(self):
        self.assertEqual("68550000", self.order1.price())

    def test9_order2_price(self):
        self.assertEqual("5500000", self.order2.price())

    def test10_order3_price(self):
        self.assertEqual("875000", self.order3.price())