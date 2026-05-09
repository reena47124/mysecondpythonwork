#oops in python
#inheritance
#add new method in child class.
class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def display(self):
        print(f"{self.name} is a {self.breed}")

class Dog(Animal):
    def info(self):
        print(f"{self.breed} is a dog.")

    def show(self):
        print(f"{self.name} barks.")

d1=Dog("bruno","golden retriever")
d1.display()
d1.info()
d1.show()
                    