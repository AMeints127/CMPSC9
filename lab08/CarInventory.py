from CarInventoryNode import *

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, car, currentNode):
        if car.make == currentNode.cars[0].make and car.model == currentNode.cars[0].model:
            currentNode.cars.append(car)
        elif car < currentNode.cars[0]:
            if currentNode.left != None:
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car, parent=currentNode)
        else:
            if currentNode.right != None:
                self._addCar(car, currentNode.right)
            else:
                currentNode.right = CarInventoryNode(car, parent=currentNode)

    def doesCarExist(self, car):
        if self.root:
            res = self._doesCarExist(car, self.root)
            if res:
                return True
            else:
                return False
        else:
            return False
    def _doesCarExist(self, car, currentNode):
        if not currentNode:
            return False
        for i in currentNode.cars:
                if car == i:
                    return True
        if car < currentNode.cars[0]:
            return self._doesCarExist(car, currentNode.left)
        else:
            return self._doesCarExist(car, currentNode.right)

    def inOrder(self):
        cs = ''
        if self.root != None:
            cs += self.inorderHelp(self.root.left)
            cs += str(self.root)
            cs += self.inorderHelp(self.root.right)
        return cs
    
    def inorderHelp(self, currentNode):
        cs = ''
        if currentNode != None:
            cs += self.inorderHelp(currentNode.left)
            cs += str(currentNode)
            cs += self.inorderHelp(currentNode.right)
        return cs

    def preOrder(self):
        if self.root != None:
            cs = str(self.root)
        else:
            return ''
        
        if self.root.left:
            cs += self.preorderHelp(self.root.left)
        if self.root.left:
            cs += self.preorderHelp(self.root.right)
        return cs
    def preorderHelp(self, currentNode):
        cs = ''
        if currentNode:
            cs += str(currentNode)
            cs += self.preorderHelp(currentNode.left)
            cs += self.preorderHelp(currentNode.right)
        return cs

    def postOrder(self):
        if self.root != None:
            cs = ''
        else:
            return ''
        if self.root.left:
            cs += self.postorderHelp(self.root.left)
        if self.root.right:
            cs += self.postorderHelp(self.root.right)
        cs += str(self.root)
        return cs

    def postorderHelp(self, currentNode):
        cs = ''
        if currentNode:
            cs += self.postorderHelp(currentNode.left)
            cs += self.postorderHelp(currentNode.right)
            cs += str(currentNode)
        return cs

    def getBestCar(self, make, model):
        searchCar = Car(make, model, 0, 0)
        CI = CarInventoryNode(searchCar)
        if self.root != None:
            res = self._getCar(CI, self.root)
        else:
            return None
        carsL = []
        if res:
            bestCar = res.cars[0]
            for i in res.cars:
                if i.year > bestCar.year:
                    bestCar = i
                elif i.year == bestCar.year:
                    if i.price > bestCar.price:
                        bestCar = i
            return bestCar
        else:
            return res

    def _getCar(self, car, currentNode):
        if not currentNode:
            return None
        elif currentNode.make == car.make and currentNode.model == car.model:
            return currentNode
        elif car < currentNode.cars[0]:
            return self._getCar(car, currentNode.left)
        else:
            return self._getCar(car, currentNode.right)

    def getWorstCar(self, make, model):
        searchCar = Car(make, model, 0, 0)
        CI = CarInventoryNode(searchCar)
        if self.root != None:
            res = self._getCar(CI, self.root)
        else:
            return None
        carsL = []
        if res:
            worstCar = res.cars[0]
            for i in res.cars:
                if i.year < worstCar.year:
                    worstCar = i
                elif i.year == worstCar.year:
                    if i.price < worstCar.price:
                        worstCar = i
            return worstCar
        else:
            return res

    def getTotalInventoryPrice(self):
        total = 0
        if self.root != None:
            total += self.priceHelp(self.root.left)
            for i in self.root.cars:
                total += i.price
            total += self.priceHelp(self.root.right)
        return total
    
    def priceHelp(self, currentNode):
        total = 0
        if currentNode != None:
            total += self.priceHelp(currentNode.left)
            for i in currentNode.cars:
                total += i.price
            total += self.priceHelp(currentNode.right)
        return total

    def getSuccessor(self, make, model):
        searchCar = Car(make, model, 0, 0)
        CI = CarInventoryNode(searchCar)
        res = self._getCar(CI, self.root)
        succ = None
        #Check if node has right subtree
        if res:
            if res.right:
                succ = self.findMin(res.right)
            elif res.parent:
                node = res.parent
                while node:
                    if node.cars[0] > res.cars[0]:
                        return node
                    else:
                        node = node.parent
            else:
                succ = None
        return succ
    


        
    def findMin(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    def findMax(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    def spliceOut(self, node):
        if (not node.right) and (not node.left):
            if node.isLeft():
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left or node.right:
            if node.right:
                if node.isLeft():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                if node.isLeft():
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
           

    def removeCar(self, make, model, year, price):
        searchCar = Car(make, model, 0, 0)
        fullCar = Car(make, model, year, price)
        CI = CarInventoryNode(searchCar)
        node = self._getCar(CI, self.root)
        if node:
            if len(node.cars) == 1:
                if node.cars[0] == fullCar:
                    self._remove(node, make, model)
                    return True
                else:
                    return False
            else:
                for i in node.cars:
                    if i == fullCar:
                        node.cars.remove(i)
                        return True
                return False
        else:
            return False

    def _remove(self, currentNode, make, model):
        if (not currentNode.left) and (not currentNode.right):
            if not currentNode.parent:
                self.root = None
            elif currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.left and currentNode.right:
            succ = self.getSuccessor(make, model)
            self.spliceOut(succ)
            currentNode.make = succ.make
            currentNode.model = succ.model
            currentNode.cars = succ.cars
        else:
            if currentNode.left:
                if currentNode.isLeft():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRight():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:
                    self.root = currentNode.left
                    currentNode.left.parent = None
            else:
                if currentNode.isLeft():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRight():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    self.root = currentNode.right
                    currentNode.right.parent = None

                
                
                

    
        

        
