#oops in python.
#demonstrate how changing class variable affects all objects.
class Employee:
    company_name="abc company"
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary

    def display(self):
        print(f"company name:{self.company_name},name:{self.name},designation:{self.designation},salary:{self.salary}") 
e1=Employee("a","ceo",10000000)
e2=Employee("b","hr",5000000)
e1.display()
e2.display()
print(f"class variable before updation:{e1.company_name}")
print(f"class variable before updation:{e2.company_name}")
Employee.company_name="xyz"
e1.display()
e2.display()
print(f"class variable after updation:{e1.company_name}")

