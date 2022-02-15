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


class CategoryTest(TestCase):
    def setUp(self) -> None:
        self.category1 = Category.objects.create(name="Self Care",
                                                 description="Medicinal and Self-Care products.")
        self.category2 = Category.objects.create(name="Electronics",
                                                 description="Consists of every electronic device ever.")
        self.category3 = Category.objects.create(name="Laptop",
                                                 description="Laptops",
                                                 category=self.category2)
        self.category4 = Category.objects.create(name="Smart Phone",
                                                 category=self.category2)

    def test2_category3_detail(self):
        self.assertEqual("Laptop", self.category3.name)
        self.assertEqual("Laptops", self.category3.description)
        self.assertEqual(self.category1, self.category3.category)

    def test3_category2_categories(self):
        self.assertIn(self.category3, self.category2.categories.all())
        self.assertIn(self.category4, self.category2.categories.all())

    def test4_category1_categories(self):
        self.assertTrue(len(self.category1.categories.all()) == 0)

# class ProductTest(TestCase):
#     def setUp(self) -> None:
#         self.discount1 = Discount.objects.create(type="VAL",
#                                                  amount="10000")
#         self.discount2 = Discount.objects.create(type="PER",
#                                                  amount="25")
#         self.discount3 = Discount.objects.create(type="PER",
#                                                  amount="40",
#                                                  max_value="20000")
