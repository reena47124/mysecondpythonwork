#oops in python.
#change class variable using class name.
class Animal:
    species="dog"
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

d1=Animal("bruno","brown")
d2=Animal("max","white")
print(d1.species)
print(d2.species)
Animal.species="cat"
d3=Animal("kitty","white")
print(d1.species)
print(d3.species)
