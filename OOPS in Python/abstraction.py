
from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def speed(self):
        pass

class Bike(Vehical):
    def speed(self):
        print("Bike Speed is 80km/h")

b = Bike()

b.speed()