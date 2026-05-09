#oops in python
#abstraction
#create abstract class shape
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        area=self.side*self.side
        print(f"area of the square:{area}")
s1=Square(4)
s1.area()
                