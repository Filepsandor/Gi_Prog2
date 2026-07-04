from Animal import Animal
from Habitat import Habitat

class Frog(Animal):
    
    weight: int
    height: int 
    habitat: list[Habitat]
    TYPE = "Frog"
    
    def __init__(self, habitat):
        self.habitat = habitat

    def sound(self):
        return "Brekk"
    
    def lives(self, habitat):
        return habitat in self.habitat