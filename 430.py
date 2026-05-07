#oops in python
#encapsulation
#validate age using setter method.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get_age(self):
        print(f"current age:{self.__age}")

    def set_age(self,age):
        if age>0 and age<=100:
            self.__age=age
            print(f"updated age is:{self.__age}")
        else:
            print(f"invalid input!")

p1=Person("a",25)
p1.get_age()
p1.set_age(22)
p1.set_age(-3)
p1.set_age(105)
