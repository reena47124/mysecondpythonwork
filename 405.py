#oops in python
#create multiple objects from one class.
class Animal:
    def __init__(self,species,name,colour):
        self.species=species
        self.name=name
        self.colour=colour
a1=Animal("dog","bruno","brown")
a2=Animal("cat","kitty","white")
print(a1.species,a1.name,a1.colour)
print(a2.species,a2.name,a2.colour) 
       