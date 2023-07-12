
class Customer: 

    def __init__(self, name, wallet, age, energy): 
        self.name = name
        self.wallet = wallet 
        self.age = age
        self.energy = energy 

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price 

    def bought_drink_energy_up(self, caffeine_level):
        self.energy + self.drink.caffeine_level