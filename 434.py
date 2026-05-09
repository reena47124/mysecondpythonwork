#oops in python
#encapsulation
#create student class with private marks:
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def display_marks(self):
        print(f"marks:{self.__marks}")
s1=Student("a",98)
print(f"name:{s1.name}") 
s1.display_marks()
