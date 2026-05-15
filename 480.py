#exceptional handling in python
#handle ZeroDivisionError
try:
    num1=int(input("enter the first value:"))
    num2=int(input("enter the second value:"))
    result=num1/num2
    print(f"result:{result}")
except ZeroDivisionError:
    print(f"cannot divide by zero")
