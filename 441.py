#oops in python
#inheritance
#create vehicle-car inheritance.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f"{self.brand} has {self.model} model.")

class Car(Vehicle):
    def __init__(self,brand,model,colour):
        super().__init__(brand,model) 
        self.colour=colour

    def details(self):
        print(f"car has {self.colour} colour.")

c1=Car("mercedes","benz","white") 
c1.display()
c1.details()
