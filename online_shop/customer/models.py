from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")


class Address(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    customer = models.ForeignKey(to="Customer", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.province}, {self.city}"
