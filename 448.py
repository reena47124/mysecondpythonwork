#oops in python
#polymorphism
#use same method on different objects.
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        self.area=self.side*self.side
        print(f"area of the square is:{self.area}")
s1=Square(2)
s2=Square(3)
s3=Square(4)
s1.area()
s2.area()
s3.area()
            