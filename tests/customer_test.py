

import unittest
from src.customer import Customer 
from src.drink import Drink 

class TestCustomer (unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Sky", 500, 32, 10)
        self.water = Drink("Spring Water", 10, 20)
        self.coffee = Drink("Double Espresso", 5, 30)

    def test_has_a_name(self):
        expected = "Sky"
        actual = self.customer.name
        self.assertEqual(expected, actual)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.water)
        self.assertEqual(490, self.customer.wallet)

    def bought_drink_energy_up(self):
        self.customer.buy_drink(self.coffee)
        self.assertEqual(40, self.customer.energy)

