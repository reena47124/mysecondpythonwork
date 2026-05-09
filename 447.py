#oops in python
#polymorphism
#create shape classes with area method.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.area=3.14*self.radius*self.radius 
        print(f"area of the circle:{self.area}")
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        self.area=self.side*self.side
        print(f"area of the square:{self.area}")
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        self.area=self.length*self.breadth
        print(f"area of the rectangle:{self.area}")
c1=Circle(7)
s1=Square(4)
r1=Rectangle(3,4)
c1.area()
s1.area()
r1.area()
                                   