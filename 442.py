#oops in python
#inheritance
#create multi-level inheritance example.
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def sound(self):
        print(f"{self.name} barks.")
class Dog(Animal):
    def __init__(self,name,breed,colour):
        super().__init__(name,breed)
        self.colour=colour

    def details(self):
        print(f"{self.name} has {self.colour} colour.") 

class Puppy(Dog):
    def show(self):
        print(f"{self.name} is a baby {self.breed} of {self.colour} colour.")

p1=Puppy("bruno","golden retriever","brown")
p1.sound()
p1.details()
p1.show()
                               