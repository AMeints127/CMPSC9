from CustomPizza import *
from SpecialtyPizza import *
from PizzaOrder import *
from OrderQueue import *

def test_customPizza():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    Price: $8.00\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("pineapple")

    assert cp2.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: L\n\
    Toppings:\n\
    \t+ pineapple\n\
    Price: $14.00\n"

def test_specialtyPizza():
    sp1 = SpecialtyPizza("S", "SMG")
    assert sp1.getPizzaDetails() == \
    "SPECIALTY PIZZA\n\
    Size: S\n\
    Name: SMG\n\
    Price: $12.00\n"

def test_pizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra garlic")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "SMG")
    order = PizzaOrder(133000) 
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
    "******\n\
    Order Time: 133000\n\
    CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    \t+ extra garlic\n\
    \t+ sausage\n\
    Price: $9.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: SMG\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $21.00\n\
    ******\n"
