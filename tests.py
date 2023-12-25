import unittest
from martian_clinic import *


class TestTypes(unittest.TestCase):
    
    customer = Customer(eyes=12, limbs=5)

    def test_customer_name_type(self):
        self.assertIsInstance(customer.name, str)

    def test_customer_surname_type(self):
        self.assertIsInstance(customer.surname, str)

    def test_customer_limbs(self):
        self.assertIsInstance(customer.limbs, int)

    def test_customer_eyes(self):
        self.assertIsInstance(customer.eyes, int)


unittest.main(argv=[''], verbosity=2, exit=False)