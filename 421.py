#oops in python.
#create Employee class with company name as class variable.
class Employee:
    company_name="abc company"
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation

e1=Employee("a","ceo")
e2=Employee("b","developer")
e3=Employee("c","hr")
print(e1.company_name,e1.name,e1.designation) 
print(e2.company_name,e2.name)
print(e3.company_name,e3.designation) 
      