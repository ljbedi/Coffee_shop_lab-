import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee = Drink("Black coffee", 3.95) 
        self.tea = Drink("Earl Grey", 2.00) 

        self.coffee_shop = CoffeeShop("The Prancing Pony", 100, [self.coffee, self.tea])
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_coffee_shop_has_drinks(self):
        self.assertEqual([self.coffee, self.tea], self.coffee_shop.drinks)
        # alternative method of checking lists as below
        self.assertEqual(2, len(self.coffee_shop.drinks))

    def test_increase_till(self): 
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)
    
    # @unittest.skip("delete this line to run the test")
    def test_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)

    

    

# A CoffeeShop should be able to sell a drink to a customer and increase it's till by the price of Drink.
# Hint: Use a Customer method you already have.