#oops in python
#create BankAccount with balance and deposit method.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("deposited amount:",amount)
        print("new amount:",self.balance)

b1=BankAccount(10000)
b1.deposit(5000)

