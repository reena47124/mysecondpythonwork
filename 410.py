#oops in python.
#create a Rectangle class and method to find area.
#method 1)
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area:",self.length*self.breadth)
r1=Rectangle(12,3)
r1.area()
