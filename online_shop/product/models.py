from django.db import models
from core.utils import price_discount
from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    PERCENTAGE_DISCOUNT = "PER"
    VALUE_DISCOUNT = "VAL"
    TYPES_OF_DISCOUNT = [
        (PERCENTAGE_DISCOUNT, "Percentage Discount"),
        (VALUE_DISCOUNT, "Value Discount"),
    ]
    type = models.CharField(max_length=3, choices=TYPES_OF_DISCOUNT)
    amount = models.CharField(max_length=20, validators=[MinValueValidator(1), MaxValueValidator(100)])
    max_value = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        price_tag = "%" if self.type == "PER" else "T"
        max_tag = ", max=" + self.max_value + "T" if self.max_value else ""
        message = f"{self.amount}{price_tag}{max_tag}"
        return message


class OffCode(models.Model):
    PERCENTAGE_DISCOUNT = "PER"
    VALUE_DISCOUNT = "VAL"
    TYPES_OF_DISCOUNT = [
        (PERCENTAGE_DISCOUNT, "Percentage Discount"),
        (VALUE_DISCOUNT, "Value Discount"),
    ]
    code = models.CharField(max_length=30)
    type = models.CharField(max_length=3, choices=TYPES_OF_DISCOUNT)
    amount = models.CharField(max_length=20)
    max_value = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        price_tag = "%" if self.type == "PER" else "T"
        max_tag = ", max=" + self.max_value + "T" if self.max_value else ""
        message = f"{self.amount}{price_tag}{max_tag}"
        return message


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
    image = models.ImageField(upload_to="product_images", null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    discount = models.ForeignKey(to=Discount, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(to=Category, blank=True)

    def final_price(self):
        return price_discount(self.price, self.discount)

    def __str__(self):
        return f"{self.name} ({self.price})"
