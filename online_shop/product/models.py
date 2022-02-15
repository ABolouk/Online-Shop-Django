from django.db import models
from core.utils import price_discount


class Discount(models.Model):
    PERCENTAGE_DISCOUNT = "PER"
    VALUE_DISCOUNT = "VAL"
    TYPES_OF_DISCOUNT = [
        (PERCENTAGE_DISCOUNT, "Percentage Discount"),
        (VALUE_DISCOUNT, "Value Discount"),
    ]
    type = models.CharField(max_length=3, choices=TYPES_OF_DISCOUNT)
    amount = models.CharField(max_length=20)
    max_value = models.CharField(max_length=20, null=True)


class DiscountCode(Discount):
    code = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.SET_NULL, related_name="categories")

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    detail = models.TextField()
    is_available = models.BooleanField(default=True)
    discount = models.ForeignKey(to=Discount, null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(to=Category)

    def final_price(self):
        return price_discount(self.price, self.discount)
