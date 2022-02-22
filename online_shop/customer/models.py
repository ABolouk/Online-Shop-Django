from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User, BaseModel


class Customer(models.Model):
    """
        # TODO: Add docstring
    """
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)

    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        permissions = [
            ("being_customer", "is a customer."),
        ]


class Address(BaseModel):
    """
        # TODO: Add docstring
    """
    customer = models.ForeignKey(to="Customer", null=True, on_delete=models.SET_NULL)
    province = models.CharField(max_length=100)  # TODO: Add choices for each province in Iran.
    city = models.CharField(max_length=100)  # TODO: Add choices for each city of selected province.
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.province}, {self.city}"

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
