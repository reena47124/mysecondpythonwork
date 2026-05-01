#oops in python
#show difference between class variable and instance variable.
class Vehicle:
    vehicle_name="car"           #class variable
    def __init__(self,name,model):
        self.name=name           #instance variable
        self.model=model

v1=Vehicle("mercedes","benz")    #objects
v2=Vehicle("maruti","suzuki") 
print(v1.vehicle_name,v1.name,v1.model)
print(v2.vehicle_name,v2.name,v2.model) 
