from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from core.models import BaseModel
from core.utils import price_discount
from product.models import Product, OffCode
from customer.models import Customer


class Order(BaseModel):
    customer = models.ForeignKey(to=Customer, on_delete=models.RESTRICT)
    off_code = models.ForeignKey(to=OffCode, null=True, blank=True, on_delete=models.SET_NULL)

    def total_price(self):
        price = 0
        for item in self.orderitem_set.all():
            price += int(item.price())
        return price_discount(price, self.off_code)

    def __str__(self):
        return f"{self.customer} {self.total_price()}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(1), ])

    def price(self):
        return str(self.number * int(self.product.final_price()))

    def __str__(self):
        return f"{self.number} {self.product.name}"
