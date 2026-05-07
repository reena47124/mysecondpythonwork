#oops in python
#override class variable in one object.
class Employee:
    company_name="abc"
    def __init__(self,name):
        self.name=name
e1=Employee("a")
e2=Employee("b")
e1.company_name="xyz"
print(f"e1 company name:{e1.company_name}") 
print(f"e2 company name:{e2.company_name}")
       