#oops in python.
#create calculator class with add,subtraction,multiplication and division methods.
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        sum=self.num1+self.num2
        print("sum:",sum)
    def subtraction(self):
        if self.num1>self.num2:
            sub=self.num1-self.num2
            print("subtraction:",sub)
        else:
            sub=self.num2-self.num1
            print("subtraction:",sub)
    def multiplication(self):
        mul=self.num1*self.num2
        print("multiplication:",mul) 
    def division(self):
        div=self.num1//self.num2
        print("division:",div)
c1=Calculator(120,30)
c1.add()
c1.subtraction()
c1.multiplication()
c1.division()
                   
                                