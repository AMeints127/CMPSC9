from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.types = {}
        
    def addAnimal(self, animal=None):
        if animal != None:
            if self.types.get(animal.species) == None:
                self.types[animal.species] = []
                self.types[animal.species].append(animal)
            else:
                self.types[animal.species].append(animal)

    def doesAnimalExist(self, animal=None):
        if self.types.get(animal.species) != None:
            for i in self.types[animal.species]:
                if i.name == animal.name:
                    if i.weight == animal.weight:
                        if i.age == animal.age:
                            return True
            return False
        else:
            return False

    def removeAnimal(self, animal=None):
        if animal != None:
            if self.types.get(animal.species) != None:
                for i in self.types[animal.species]:
                    if i.name == animal.name:
                        if i.weight == animal.weight:
                            if i.age == animal.age:
                                self.types[animal.species].remove(animal)
                                return True
                return False
            else:
                return False
        else:
            return False
       

    def removeSpecies(self, species=None):
        if species != None:
            uSpecies = species.upper()
            if uSpecies in self.types:
                del self.types[uSpecies]
            else:
                return False
        else:
            return False


    def getAnimalsBySpecies(self, species=None):
        if species != None:
            uSpecies = species.upper()
        
            if self.types.get(uSpecies) == None:
                return ""

            speciesStr = ""
            lenSpecies = len(self.types[uSpecies])
            j = 1
            for i in self.types[uSpecies]:
                if j < lenSpecies:
                    speciesStr += i.toString() + '\n'
                else:
                    speciesStr += i.toString()
                j +=1

            return speciesStr
                
        else:
            return ""


        










