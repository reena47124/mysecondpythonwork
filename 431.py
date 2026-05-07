#oops in python
#encapsulation
#create a BankAccount with private balance.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        print(f"balance:{self.__balance}")

b1=BankAccount("a",1000000)
b1.get_balance()
print(f"name:{b1.name}")
        