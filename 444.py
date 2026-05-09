#oops in python
#inheritance
#create multiple inheritance.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def details(self):
        print(F"{self.name} has {self.marks} marks.")

class Library:
    def __init__(self,books):
        self.books=books

    def access(self):
        print(f"access books:{self.books}")

class School(Student,Library): 
    def __init__(self,name,marks,books):
        Student.__init__(self,name,marks)
        Library.__init__(self,books)

    def show(self):
        print(f"{self.name} got {self.marks} marks by reading {self.books} book.")

s1=School("a",98,"formulas of mathematics")
s1.details()
s1.access()
s1.show()
