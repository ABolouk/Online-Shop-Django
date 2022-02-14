from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    detail = models.TextField()
    is_available = models.BooleanField(default=True)
    discount = models.ManyToManyField(to="Discount")
    category = models.ManyToManyField(to="Category")


class Discount(models.Model):
    PERCENTAGE_DISCOUNT = "PER"
    VALUE_DISCOUNT = "VAL"
    TYPES_OF_DISCOUNT = [
        (PERCENTAGE_DISCOUNT, "Percentage Discount"),
        (VALUE_DISCOUNT, "Value Discount"),
    ]
    type = models.CharField(max_length=3, choices=TYPES_OF_DISCOUNT)
    amount = models.CharField(max_length=20)
    max_value = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    category = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
