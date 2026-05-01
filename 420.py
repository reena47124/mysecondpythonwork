#oops in python
#count how many objects are created using class variable.
class Student:
    count=0
    def __init__(self, name):
        self.name=name
        Student.count+=1

s1=Student("a")
s2=Student("b")
s3=Student("c") 
s4=Student("d")
print(f"total objects are created:{Student.count}")
