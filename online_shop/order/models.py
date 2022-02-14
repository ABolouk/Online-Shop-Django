from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from product.models import Product, DiscountCode
from customer.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(to="Customer", on_delete=models.CASCADE)
    discount_code = models.ForeignKey(to=DiscountCode, null=True, on_delete=models.SET_NULL)


class OrderItem(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(1), ])
