#oops in python
#create a class car with brand and model, and add a method display_info() to print car details.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print("brand:",self.brand)
        print("model:",self.model)
c1=Car("mercedes","benz")
c2=Car("maruti","suzuki")
c1.display_info()
c2.display_info()

