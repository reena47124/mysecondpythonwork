#oops in python
#create a circle class and method tp find circumference.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return(2*3.14*self.radius)
c1=Circle(4)
print("circumference:",c1.circumference())
        