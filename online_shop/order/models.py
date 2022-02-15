from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from product.models import Product, DiscountCode
from customer.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    discount_code = models.ForeignKey(to=DiscountCode, null=True, on_delete=models.SET_NULL)

    def total_price(self):
        price = 0
        for item in self.orderitem_set.all():
            price += int(item.price())

        # TODO Add discount method, or move final price method in product to core.utils and use it here

    def __str__(self):
        return f"{self.customer} {self.price()}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(1), ])

    def price(self):
        return str(self.number * int(self.product.final_price()))

    def __str__(self):
        return f"{self.number} {self.product.name}"
