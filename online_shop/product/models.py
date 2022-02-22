from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from core.utils import price_discount
from core.models import BaseModel


class AbstractDiscount(BaseModel):
    class Meta:
        abstract = True

    PERCENTAGE_DISCOUNT = "PER"
    VALUE_DISCOUNT = "VAL"
    TYPES_OF_DISCOUNT = [
        (PERCENTAGE_DISCOUNT, _("Percentage Discount")),
        (VALUE_DISCOUNT, _("Value Discount")),
    ]
    type = models.CharField(max_length=3, choices=TYPES_OF_DISCOUNT)
    amount = models.CharField(max_length=20)  # TODO: If type==PER validate "0 < amount < 100"
    max_value = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        price_tag = "%" if self.type == "PER" else "T"
        max_tag = ", max=" + self.max_value + "T" if self.max_value else ""
        message = f"{self.amount}{price_tag}{max_tag}"
        return message


class Discount(AbstractDiscount):
    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    name = models.CharField(max_length=100, help_text=_("A name for discount."))


class OffCode(AbstractDiscount):
    class Meta:
        verbose_name = _("Discount Code")
        verbose_name_plural = _("Discount Codes")

    code = models.CharField(max_length=30, help_text=_("Code that validates the discount."))


class Category(models.Model):
    name = models.CharField(max_length=100)
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
    image = models.ImageField(upload_to="product_images", null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    discount = models.ForeignKey(to=Discount, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(to=Category, blank=True)

    def final_price(self):
        return price_discount(self.price, self.discount)

    def __str__(self):
        return f"{self.name} ({self.price})"
