from Animal import Animal
from Habitat import Habitat

class Fox(Animal):

    weight: int
    height: int 
    habitat: Habitat
    TYPE = "Fox"
    
    def __init__(self, habitat: Habitat, weight:int = 10, height:int = 30) -> None:
        self.habitat = habitat
        if weight > 100:
            raise ValueError('Fox is too heavy')
        self. weight = weight
        assert height>=100, ValueError('Fox is too tall')
        self. height = height
        
    def __str__(self) -> str:
        return f"FOX: {self.weight}, {self.height}, {self.habitat.value}"
    
    def sound(self):
        return "Vau"
    
    def lives(self, habitat):
        return self.habitat == habitat
    