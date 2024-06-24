from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    b1 = Beverage(12, 10.05)
    b2 = Beverage(12)
    b3 = Beverage(price = 20.5)

    b1.updateOunces(16)
    b1.updatePrice(20.5)
    
    assert b1.getInfo() == '16 oz, $20.50'
    assert b1.getOunces() == 16
    assert b1.getPrice() == 20.5
    assert b2.getPrice() == None
    assert b3.getOunces() == None

def test_Coffee():
    c1 = Coffee(6, 5.0, "Latte")
    
    c1.updateOunces(10)
    c1.updatePrice(10)

    assert c1.getOunces() == 10
    assert c1.getPrice() == 10
    assert c1.getInfo() == "Latte Coffee, 10 oz, $10.00"

def test_FruitJuice():
    f1 = FruitJuice(12, 8.1, "Apple")
    f2 = FruitJuice(12, 8.1, ["Apple", "Banana"])

    f1.updateOunces(16)
    f1.updatePrice(11.2)

    assert f1.getInfo() == "Apple Juice, 16 oz, $11.20"
    assert f1.getOunces() == 16
    assert f1.getPrice() == 11.2
    assert f2.getInfo() == "Apple/Banana Juice, 12 oz, $8.10"

def test_DrinkOrder():
    order = DrinkOrder()
    c1 = Coffee(6, 5.0, "Latte")
    c2 = Coffee(6, 5.0, "Espresso")
    f1 = FruitJuice(12, 8.1, "Apple")
    f2 = FruitJuice(12, 8.1, ["Apple", "Banana"])
    order.addBeverage(c1)
    order.addBeverage(c2)
    order.addBeverage(f1)
    order.addBeverage(f2)
    assert order.getTotalOrder() == "Order Items:\n* Latte Coffee, 6 oz, $5.00\n* Espresso Coffee, 6 oz, $5.00\n* Apple Juice, 12 oz, $8.10\n* Apple/Banana Juice, 12 oz, $8.10\nTotal Price: $26.20"

    order2 = DrinkOrder()
    c1 = Coffee(ounces=6, style="Latte")
    c2 = Coffee(6, 5.0, "Espresso")
    f1 = FruitJuice(12, 8.1, "Apple")
    f2 = FruitJuice(12, 8.1, ["Apple", "Banana"])
    order2.addBeverage(c1)
    order2.addBeverage(c2)
    order2.addBeverage(f1)
    order2.addBeverage(f2)
    assert order2.getTotalOrder() == "Order Items:\n* Latte Coffee, 6 oz, $0.00\n* Espresso Coffee, 6 oz, $5.00\n* Apple Juice, 12 oz, $8.10\n* Apple/Banana Juice, 12 oz, $8.10\nTotal Price: $21.20"


    


    

