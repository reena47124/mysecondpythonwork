#oops in python
#polymorphism
#compare objects using magic methods
class Student:
    def __init__(self,marks):
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
s1=Student(98)
s2=Student(90)
if s1>s2:
    print(f"s1 has greater marks.")
else:
    print(f"s2 has greater marks")
            