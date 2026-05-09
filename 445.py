#oops in python
#polymorphism
#create animal class with sound() method and override sound() in dog and cat.
class Animal:
    def sound(self):
        print(f"all animals speak different languages.")
class Dog(Animal):
    def sound(self):
        print(f"dog barks!")
class Cat(Animal):
    def sound(self):
        print(f"cat meows!")
d1=Dog()
d1.sound()
c1=Cat()
c1.sound()

                