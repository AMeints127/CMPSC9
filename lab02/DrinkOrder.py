from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        order_str = ""
        total = 0
        for i in self.drinks:
            order_str += "* " + i.getInfo() + '\n'
            if i.price != None:
                total += i.price

        return "Order Items:" + '\n' + order_str + f"Total Price: ${total:.2f}"


