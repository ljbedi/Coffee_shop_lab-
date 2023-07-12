import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer 

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee = Drink("Black coffee", 3.95, 50) 
        self.tea = Drink("Earl Grey", 2.00, 45) 
        self.customer = Customer("Eilein", 50, 21, 100)

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

    def test_sell_drink(self):
        self.coffee_shop.sell_drink(self.coffee, self.customer)
        self.assertEqual(103.95, self.coffee_shop.till)
        self.assertEqual(46.05, self.customer.wallet)


        # self.coffee_shop.till += self.coffee.price
        # self.assertEqual(103.95, self.coffee_shop.till)

    def test_check_age(self):
        if self.customer.age >= 16:
            self.coffee_shop.till += self.coffee.price
            self.assertEqual(103.95, self.coffee_shop.till)
        else:
            self.assertEqual(100, self.coffee_shop.till)

    

    
