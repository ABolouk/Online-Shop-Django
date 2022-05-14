from django.test import TestCase

from product.models import Product, Category, Brand
from product.serializers import ProductSerializer


class ProductSerializerTest(TestCase):

    def setUp(self) -> None:
        category = Category.objects.create(name="Electronics", description="Consists of every electronic device ever.")
        brand = Brand.objects.create(name="ASUS")
        product = Product.objects.create(name="Zephyrus", brand=brand, price="56000000", detail="Blah Blah Blah",
                                         is_available=False)
        product.category.add(category)

    def test_serializer(self):
        product = Product.objects.all()[0]
        product_serializer = ProductSerializer(instance=product)
        print(product_serializer.data)

    # def test_deserializer(self):
        # data =
