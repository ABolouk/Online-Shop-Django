from django.test import TestCase
from product.models import Product, Discount, DiscountCode, Category


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount = Discount.objects.create(type="PER",
                                                amount="40",
                                                max_value="20000")

    def test1_discount_detail(self):
        self.assertEqual("PER", self.discount.type)
        self.assertFalse("per" == self.discount.type)
        self.assertEqual("40", self.discount.amount)
        self.assertEqual("20000", self.discount.max_value)
