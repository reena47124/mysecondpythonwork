#oops in python
#polymorphism
#operator overloading with +
class Number:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        self.add=self.value+other.value
        print(f"addition:{self.add}")

n1=Number(10)
n2=Number(12)
result=n1+n2
print(f"addition:{result}")


