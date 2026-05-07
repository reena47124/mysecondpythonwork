#oops in python
#encapsulation
#create class with private variable --salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name        #public_variable
        self.__salary=salary  #private_variable

e1=Employee("a","1 lakh")
print(f"name:{e1.name}")
print(f"salary:{e1._Employee__salary}")    #accessing private variable indirectly      