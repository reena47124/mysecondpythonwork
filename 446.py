#oops in python
#polymorphism
#loop through objects and call same method.
class Dog:
    def sound(self):
        print(f"dog barks!")
class Cat:
    def sound(self):
        print(f"cat meows!")
class Bird:
    def sound(Self):
        print(f"birds chirpes!") 
animals=[Dog(),Cat(),Bird()]
for animal in animals:
    animal.sound()
                           