from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces=None, price=None, fruits=None):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        bevInfo = super().getInfo()
        allStyle = ''
        if type(self.fruits) == list:
            allStyle = "/".join(str(i) for i in self.fruits)
        else:
            allStyle = self.fruits

        return f"{allStyle} Juice, {bevInfo}"

