#oops in python
#inheritance
#create hierarchical inheritance example.
class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Employee(Person):
    def salary_employee(self):
        print(f"{self.name} works as an employee and has {self.salary} salary.")
class Intern(Person):
    def salary_intern(self):
        print(f"{self.name} works as an intern and has {self.salary} salary.")
e1=Employee("a",100000)
e1.salary_employee()
i1=Intern("b",20000)
i1.salary_intern()

