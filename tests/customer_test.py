

import unittest
from src.customer import Customer 
from src.drink import Drink 

class TestCustomer (unittest.TestCase):

    def setUp(self):
        self.sky = Customer("Sky", 50)
        self.water = Drink("Spring Water", 10)

    def test_has_a_name(self):
        expected = "Sky"
        actual = self.sky.name
        self.assertEqual(expected, actual)

    def test_customer_can_buy_drink(self):
        self.sky.buy_drink(self.water)
        self.assertEqual(40, self.sky.wallet)