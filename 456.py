#oops in python
#abstraction
#create abstract class vehicle,implement bike and car.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def average(self):
        pass
class Bike(Vehicle):
    def __init__(self,distance,fuel):
        self.distance=distance 
        self.fuel=fuel
    def average(self):
        average=self.distance//self.fuel
        print(f"average given by bike:{average}")
class Car(Vehicle):
    def __init__(self,distance,fuel):
        self.distance=distance 
        self.fuel=fuel
    def average(self):
        average=self.distance//self.fuel
        print(f"average given by car:{average}") 
b1=Bike(24,2)
b1.average()
c1=Car(45,3)
c1.average()

