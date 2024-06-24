from Car import *

class CarInventoryNode():
    def __init__(self, car, left=None, right=None, parent=None):
        self.car = car
        self.make = self.car.make
        self.model = self.car.model
        self.year = self.car.year
        self.price = self.car.price
        
        self.cars = []
        self.cars.append(self.car)
        
        self.parent = parent
        self.left = left
        self.right = right

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right

    def isLeft(self):
        return self.parent and self.parent.left == self
    def isRight(self):
        return self.parent and self.parent.right == self

    def replaceData(self, currentNode, left, right):
        self.car = currentNode
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __str__(self):
        carStr = ''
        for i in self.cars:
            carStr += str(i) + '\n'

        return carStr

            
        
