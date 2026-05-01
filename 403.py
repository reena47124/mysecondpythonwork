#oops in python
#create a class car with brand and model.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
c1=Car("mercedes","benz")
c2=Car("maruti","suzuki")
print(c1.brand,c1.model)
print(c2.brand,c2.model)
        