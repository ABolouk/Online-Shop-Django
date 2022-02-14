from django.db import models
from product.models import Product, DiscountCode
from customer.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(to="Customer", on_delete=models.CASCADE)
    discount_code = models.ForeignKey(to=DiscountCode, null=True, on_delete=models.SET_NULL)
