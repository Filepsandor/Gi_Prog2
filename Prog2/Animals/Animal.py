from abc import abstractmethod, ABC

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def lives(self, habitat):
        pass