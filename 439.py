#oops in python
#inheritance
#override parent method in child class
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def display(self):
        print(f"{self.name} is a {self.breed}")

class Dog(Animal):
    def display(self):
        print(f"{self.name} barks")      #method override

d1=Dog("bruno","golden retriever")
d1.display()

