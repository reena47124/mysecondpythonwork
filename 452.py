#oops in python
#polymorphism
#create polymorphic payment system.
class CreditCard:
    def pay(self,amount):
        print(f"{amount} is paid using credit card.")
class UPI:
    def pay(self,amount):
        print(f"{amount} is paid using UPI.")
class DebitCard:
    def pay(self,amount):
        print(f"{amount} is paid using debit card.") 
class Cash:
    def pay(self,amount):
        print(f"{amount} is paid using cash.")
def payment_method(method,amount):
    method.pay(amount)

c1=CreditCard()
u1=UPI()
d1=DebitCard()
ca1=Cash()
payment_method(c1,10000)
payment_method(u1,1200)
payment_method(d1,3000)
payment_method(ca1,770)
