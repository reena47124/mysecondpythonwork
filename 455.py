#oops in python
#abstract
#create abstract class shape, add abstract method area(), implement rectanlge and circle classes.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        print(f"area of the rectangle:{area}")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        area=3.14*self.r*self.r
        print(f"area of the circle:{area}")
r1=Rectangle(3,4)
r1.area()
c1=Circle(7)
c1.area()
                            
