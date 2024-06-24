from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size, price=0.0)
        self.toppings = []
        if self.size == "S":
            self.price = 8.00
        elif self.size == "M":
            self.price = 10.00
        elif self.size == "L":
            self.price = 12.00

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        elif self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        toppingstr = ''
        
        for i in self.toppings:
            toppingstr += '\t+ ' + str(i) + '\n'

        return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}Price: ${:.2f}\n"\
               .format(self.size, toppingstr, self.price)

