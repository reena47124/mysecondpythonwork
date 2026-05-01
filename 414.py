#oops in python
#create BankAccount with balance and deposit method, and add withdraw method in BankAccount.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("deposited amount:",amount)
        print("new amount:",self.balance)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawn amount:",amount)
            print("new balance:",self.balance)
        else:
            print("insuffiencent balance!")       

b1=BankAccount(10000)
b1.deposit(50000)
b1.withdraw(20000)
