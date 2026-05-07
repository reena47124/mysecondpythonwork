#oops in python
#print namespace of object and class.
class Student:
    school_name="abc school"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("a",98)
s2=Student("b",90)
print(f"class namespace:{Student.__dict__}")
print(f"first object namespace:{s1.__dict__}")
print(f"second object namespace:{s2.__dict__}")        