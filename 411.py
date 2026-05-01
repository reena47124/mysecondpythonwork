#oops in python.
#create a Rectangle class and method to find area.
#method 2)
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
r1=Rectangle(12,4)
print("area:",r1.area())
