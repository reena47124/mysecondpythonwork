#oops in python
#encapsulation
#restrict direct modification of balance.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

#b1=BankAccount("a",100000)
#print(b1.self.__balance)  #error
#print(b1._BankAccount__balance)    #indirect access

    def get_balance(self):
        print(f"current balance:{self.__balance}")

    def set_balance(self,amount):
        self.__balance+=amount
        print(f"updated balance:{self.__balance}")

b2=BankAccount("b",200000)
b2.get_balance()
b2.set_balance(100000)



