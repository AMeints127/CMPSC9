from Apartment import *
from lab06 import *

#Apartment
def test___gt__():
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(5000, 600, "average")
    assert (a0 > a1) == False
    assert (a1 > a0) == True

def test___lt__():
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(5000, 600, "average")
    assert (a0 < a1) == True
    assert (a1 < a0) == False

def test___eq__():
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(5000, 600, "average")
    a3 = Apartment(1204, 200, "bad")
    assert (a0 == a1) == False
    assert (a0 == a3) == True

#lab06
def test_mergesort():
    a0 = Apartment(1120, 300, "bad")
    a1 = Apartment(5000, 300, "average")
    a2 = Apartment(950, 300, "excellent")
    a3 = Apartment(2000, 200, "excellent")
    a4 = Apartment(950, 200, "excellent")
    a5 = Apartment(500, 350, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    mergesort(apartmentList)
    assert apartmentList == [a5, a4, a2, a0, a3, a1]

def test_ensureSortedAscending():
    a0 = Apartment(1120, 300, "bad")
    a1 = Apartment(5000, 300, "average")
    a2 = Apartment(950, 300, "excellent")
    a3 = Apartment(2000, 200, "excellent")
    a4 = Apartment(950, 200, "excellent")
    a5 = Apartment(500, 350, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getBestApartment():
    a0 = Apartment(1120, 300, "bad")
    a1 = Apartment(5000, 300, "average")
    a2 = Apartment(950, 300, "excellent")
    a3 = Apartment(2000, 200, "excellent")
    a4 = Apartment(950, 200, "excellent")
    a5 = Apartment(500, 350, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getBestApartment(apartmentList) == a5.getApartmentDetails()

def test_getWorstApartment():
    a0 = Apartment(1120, 300, "bad")
    a1 = Apartment(5000, 300, "average")
    a2 = Apartment(950, 300, "excellent")
    a3 = Apartment(2000, 200, "excellent")
    a4 = Apartment(950, 200, "excellent")
    a5 = Apartment(500, 350, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getWorstApartment(apartmentList) == a1.getApartmentDetails()


def test_getAffordableApartments():
    a0 = Apartment(1120, 300, "bad")
    a1 = Apartment(5000, 300, "average")
    a2 = Apartment(950, 300, "excellent")
    a3 = Apartment(2000, 200, "excellent")
    a4 = Apartment(950, 200, "excellent")
    a5 = Apartment(500, 350, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getAffordableApartments(apartmentList, 500) == "(Apartment) Rent: $500, Distance From UCSB: 350m, Condition: bad"


