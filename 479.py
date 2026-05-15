#exceptional handling in python
#write a program that divides two numbers usinf try-except.
try:
    num1=int(input("enter the first value:"))
    num2=int(input("enter the second value:"))
    result=num1/num2
    print(f"result:{result}")
except ZeroDivisionError:
    print(f"cannot divide by zero")
except ValueError:
    print(f"please enter the valid input")
            