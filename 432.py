#oops in python
#encapsulation
#allow deposit only through methods.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"balance after deposit:{self.__balance}")
b1=BankAccount("a",200000)
b1.deposit(100000)
            

