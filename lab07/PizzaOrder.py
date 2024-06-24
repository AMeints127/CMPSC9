from CustomPizza import *
from SpecialtyPizza import *

class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.pizzas = []
        self.maxDiff = None

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        totalPrice = 0
     
        orders = '******\nOrder Time: {}\n'.format(self.time)
        for i in self.pizzas:
            orders += i.getPizzaDetails() + '\n' + '----\n'
            totalPrice += i.price

        orders += 'TOTAL ORDER PRICE: ${:.2f}\n******\n'.format(totalPrice)

        return orders

