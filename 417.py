#oops in python.
#create a class variable school_name in Student.
class Student:
    school_name="DPS school"
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

s1=Student("ram",98)
s2=Student("laxmi",89)
print(s1.school_name,s1.name,s1.grade)
print(s2.school_name)
        
