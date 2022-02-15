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
        total_price = str(price)
        if self.discount_code:
            amount = int(self.discount_code.amount)
            try:
                max_value = int(self.discount_code.max_value)
            except:
                max_value = 0
            if self.discount_code.type == "PER":
                profit = int(price * amount / 100)
                total_price = str((price - profit) if not max_value else (price - min(max_value, profit)))
            else:
                total_price = str((price - amount) if (price >= amount) else 0)
        return total_price
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
