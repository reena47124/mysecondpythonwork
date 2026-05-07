#oops in python
#encapsulation
#create getter and setter for age.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get_age(self):
        print(f"age:{self.__age}")

    def set_age(self,age):
        self.__age=age
        print(f"age after updation:{self.__age}") 

p1=Person("a",25)
p1.get_age()
p1.set_age(22)

