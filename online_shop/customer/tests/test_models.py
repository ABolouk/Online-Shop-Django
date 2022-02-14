from django.test import TestCase
from customer.models import Customer, Address
from datetime import date


class CustomerTest(TestCase):
    def setUp(self) -> None:
        self.customer1 = Customer.objects.create(first_name="amir",
                                                 last_name="bolouk",
                                                 birth_date=date(1997, 5, 21))
        self.customer2 = Customer.objects.create(first_name="akbar",
                                                 last_name="babaii",
                                                 birth_date=date(1961, 11, 2))

    def test1_address1_(self):
        pass
