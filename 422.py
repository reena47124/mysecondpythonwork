#oops in python.
#use instance variable for salary.
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
