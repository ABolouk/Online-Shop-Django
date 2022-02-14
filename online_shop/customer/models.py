from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()


class Address(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    details = models.TextField()
    customer = models.ForeignKey(to="Customer", on_delete=models.CASCADE)
