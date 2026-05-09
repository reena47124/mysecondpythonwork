#oops in python
#real world mini project
#bank management system
class BankAccount:
    bank_name="ABC bank"
    def __init__(self,name,balance,bankAccount_number):
        self.name=name
        self.__balance=balance
        self.bankAccount_number=bankAccount_number

    def deposit(self,amount):
        self.__balance+=amount
        print(f"{amount} has been deposited successfully") 
        print(f"updated balance after deposition:{self.__balance}")  

    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print(f"{amount} has been withdrawn successfully")
            print(f"updated balance after withdrawn:{self.__balance}")
        else:
            print(f"insufficient balance!!!")

    def check_balance(self):
        print(f"current balance:{self.__balance}")

    def display(self):
        print(f"Bank account details:")
        print(f"Bank Account Number:{self.bankAccount_number}")
        print(f"Bank holder name:{self.name}")
        print(f"Current balance:{self.__balance}")

b1=BankAccount("Radha",3500000,1234567)
b1.deposit(2000000)
b1.withdraw(100000)
b1.check_balance()
b1.display()
                             