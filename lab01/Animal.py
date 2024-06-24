class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        if species != None:
            self.species = species.upper()
        else:
            self.species = species
        self.weight = weight
        self.age = age
        if name != None:
            self.name = name.upper()
        else:
            self.name = name
        
    def setSpecies(self, species=None):
        if species != None:
            self.species = species.upper()
        else:
            self.species = species

    def setWeight(self, weight):
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setName(self, name=None):
        if name != None:
            self.name = name.upper()
        else:
            self.name = name

    def toString(self):
        return ("Species: {}, Name: {}, Age: {}, Weight: {}"\
              .format(self.species, self.name, self.age, self.weight))



