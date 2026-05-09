#oops in python
#inheritance
#use super() in child constructor
class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

    def display(self):
        print(f"{self.name} is a {self.breed}")

d1=Dog("bruno","golden retriever")
d1.display()
                