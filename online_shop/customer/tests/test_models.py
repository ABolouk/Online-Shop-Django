from django.test import TestCase
from customer.models import Customer, Address
from datetime import date


class CustomerTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(first_name="amir",
                                                last_name="bolouk",
                                                birth_date=date(1997, 5, 21))

    def test1_customer_name(self):
        self.assertEqual("amir", self.customer.first_name)
        self.assertEqual("bolouk", self.customer.last_name)
        self.assertEqual("amir bolouk", self.customer.full_name())

    def test2_customer_birthdate(self):
        self.assertEqual(1997, self.customer.birth_date.year)
        self.assertEqual(5, self.customer.birth_date.month)
        self.assertEqual(21, self.customer.birth_date.day)


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

    def test3_address1_details(self):
        self.assertEqual("تهران", self.address1.province)
        self.assertEqual("تهران", self.address1.city)
        self.assertEqual("میدان انقلاب - کارگر شمالی - کوچه ۵- ساختمان اکبر- طبقه منفی ۸", self.address1.detail)
        self.assertEqual(self.customer2, self.address1.customer)

    def test4_address3_detail(self):
        self.assertEqual("", self.address3.detail)

    def test5_customer1_addresses(self):
        # self.assertIn(,self.customer1.address_set)
        print(self.customer1.address_set)
