from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    detail = models.TextField()
    is_available = models.BooleanField(default=True)
    # discount = models.ManyToManyField(to="Discount")
    # category = models.ManyToManyField(to="Category")
