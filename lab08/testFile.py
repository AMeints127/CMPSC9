from Car import *
from CarInventoryNode import *
from CarInventory import *

#Car
def test___gt__():
    A = Car("Honda", "CRV", 2009, 10000)
    B = Car("Honda", "CRV", 2007, 8000)
    assert (A > B) == True
def test___lt__():
    A = Car("Honda", "CRV", 2009, 10000)
    B = Car("Honda", "CRV", 2007, 8000)
    assert (A < B) == False
def test___eq__():
    A = Car("Honda", "CRV", 2009, 10000)
    B = Car("Honda", "CRV", 2007, 8000)
    C = Car("Honda", "CRV", 2007, 8000)
    assert (A == B) == False
    assert (B == C) == True
def test___str__():
    A = Car("Honda", "CRV", 2009, 10000)
    assert str(A) == 'Make: HONDA, Model: CRV, Year: 2009, Price: $10000'

#CarInventoryNode
def test___str__():
    A = Car("Honda", "CRV", 2009, 10000)
    B = Car("Honda", "CRV", 2007, 8000)
    carNode = CarInventoryNode(A)
    carNode.cars.append(B)
    assert str(carNode) == \
    'Make: HONDA, Model: CRV, Year: 2009, Price: $10000\n\
Make: HONDA, Model: CRV, Year: 2007, Price: $8000\n'

#CarInventory
def test_addCar():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.inOrder() == \
'Make: HONDA, Model: CIVIC, Year: 2020, Price: $20000\n\
Make: MAZDA, Model: CX5, Year: 2019, Price: $23000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2022, Price: $45000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2018, Price: $30000\n'
    
def test_doesCarExist():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)
    E = Car("Nissan", "Leaf", 2015, 15000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.doesCarExist(A) == True
    assert carInv.doesCarExist(E) == False
def test_inOrder():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.inOrder() == \
'Make: HONDA, Model: CIVIC, Year: 2020, Price: $20000\n\
Make: MAZDA, Model: CX5, Year: 2019, Price: $23000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2022, Price: $45000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2018, Price: $30000\n'
def test_preOrder():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.preOrder() == \
'Make: MAZDA, Model: CX5, Year: 2019, Price: $23000\n\
Make: HONDA, Model: CIVIC, Year: 2020, Price: $20000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2022, Price: $45000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2018, Price: $30000\n'
def test_postOrder():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.postOrder() == \
'Make: HONDA, Model: CIVIC, Year: 2020, Price: $20000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2022, Price: $45000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2018, Price: $30000\n\
Make: MAZDA, Model: CX5, Year: 2019, Price: $23000\n'
def test_getBestCar():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.getBestCar('Mercedes', 'Maybach') == C
def test_getWorstCar():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.getWorstCar('Mercedes', 'Maybach') == D
def test_getTotalInventoryPrice():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.getTotalInventoryPrice() == 118000

def test_getSuccessor():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.getSuccessor('Mazda', 'CX5') ==  C
    assert carInv.getSuccessor('Honda', 'Civic') == A

def test_removeCar():
    carInv = CarInventory()

    A = Car("Mazda", "CX5", 2019, 23000)
    B = Car("Honda", "Civic", 2020, 20000)
    C = Car("Mercedes", "Maybach", 2022, 45000)
    D = Car("Mercedes", "Maybach", 2018, 30000)

    carInv.addCar(A)
    carInv.addCar(B)
    carInv.addCar(C)
    carInv.addCar(D)

    assert carInv.removeCar("Mercedes", "Maybach", 2022, 45000) == True
    assert carInv.removeCar("Mercedes", "Maybach", 2022, 20000) == False

    assert carInv.inOrder() == \
'Make: HONDA, Model: CIVIC, Year: 2020, Price: $20000\n\
Make: MAZDA, Model: CX5, Year: 2019, Price: $23000\n\
Make: MERCEDES, Model: MAYBACH, Year: 2018, Price: $30000\n'

    

    
    
    











