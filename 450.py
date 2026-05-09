#oops in python
#polymorphism
#demonstrate duck typing
class Dog:
    def sound(self):
        print(f"dog barks!")
class Cat:
    def sound(self):
        print(f"cat meows!") 
class Bird:
    def sound(self):
        print(f"bird chirpes!")
def make_sound(Animal):
    Animal.sound()
d1=Dog()
c1=Cat()
b1=Bird()
make_sound(d1)
make_sound(c1)
make_sound(b1) 
