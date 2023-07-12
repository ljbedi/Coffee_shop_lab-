

import unittest
from src.customer import Customer 
from src.drink import Drink 

class TestCustomer (unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Sky", 50, 17)
        self.water = Drink("Spring Water", 10)

    def test_has_a_name(self):
        expected = "Sky"
        actual = self.customer.name
        self.assertEqual(expected, actual)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.water)
        self.assertEqual(40, self.customer.wallet)