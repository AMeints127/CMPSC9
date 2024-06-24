class Beverage:
    def __init__(self, ounces=None, price=None):
        self.ounces = ounces
        self.price = price

    def updateOunces(self, newOunces=None):
        self.ounces = newOunces

    def updatePrice(self, newPrice=None):
        self.price = newPrice

    def getOunces(self=None):
        return self.ounces

    def getPrice(self=None):
        return self.price

    def getInfo(self):
        if self.price != None:
            return f"{self.ounces} oz, ${self.price:.2f}"
        else:
            noPrice = 0.0
            return f"{self.ounces} oz, ${noPrice:.2f}"

