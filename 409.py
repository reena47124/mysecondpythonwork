#oops in python
#create a class Employee using __init__,and create method show_details() in Employee.
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show_details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
e1=Employee("radha",22,"1.5 lakhs") 
e2=Employee("kanha",24,"2 lakhs")
e1.show_details()
e2.show_details()
       
