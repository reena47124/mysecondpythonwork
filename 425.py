#oops in python
#create static data shared among all objects.
class Student:
    school_name="abc school"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"school:{Student.school_name}")
        print(f"name:{self.name}")
        print(f"marks:{self.marks}")

s1=Student("a",98) 
s2=Student("b",90)
s1.display()
s2.display()
           