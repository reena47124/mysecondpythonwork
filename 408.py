#oops in python
#change object attribute values after creation.
class Dog:
    def __init__(self,species,name,age):
        self.species=species
        self.name=name
        self.age=age
d1=Dog("labrador","max","1")
d2=Dog("rot","bruno","2")
print(d1.name,d1.species)
d1.name="cutie"
print(d1.name,d1.species)
print(f"dog1 age:{d1.age},dog2 age:{d2.age}")
d1.age=3
print(f"dog1 age:{d1.age},dog2 age:{d2.age}")

