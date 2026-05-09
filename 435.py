#oops in python
#encapsulation
#explain name mangling with example
class Student:
    def __init__(self,name,subject,marks):
        self.name=name
        self.subject=subject
        self.__marks=marks
s1=Student("a","maths",98)
#print(s1.marks)    #error
print(f"name:{s1.name},subject:{s1.subject},marks:{s1._Student__marks}")

