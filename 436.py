#oops in python
#inheritance
#create class animal and child class dog.
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
class Dog(Animal):
    def display(self):
        print(f"{self.name} is a {self.breed}")

d1=Dog("bruno","golden retriever")
d1.display()
        
  
