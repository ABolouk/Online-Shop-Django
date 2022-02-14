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

    def test1_customer1_(self):
        pass


class AddressTest(TestCase):
    def setUp(self) -> None:
        self.customer1 = Customer.objects.create(first_name="amir",
                                                 last_name="bolouk",
                                                 birth_date=date(1997, 5, 21))
        self.customer2 = Customer.objects.create(first_name="akbar",
                                                 last_name="babaii",
                                                 birth_date=date(1961, 11, 2))
        self.address1 = Address.objects.create(province="تهران",
                                               city="تهران",
                                               detail="میدان انقلاب - کارگر شمالی - کوچه ۵- ساختمان اکبر- طبقه منفی ۸",
                                               customer=self.customer2)
        self.address2 = Address.objects.create(province="Guilan",
                                               city="Rasht",
                                               detail="Yakhsazi Sq., Andisheh Sh., 5th St., No.16",
                                               customer=self.customer1)
        self.address3 = Address.objects.create(province="فارس",
                                               city="شیراز",
                                               customer=self.customer1)
