#exceptional handling in python
#handle invalid integer input using ValueError
try:
    a=input("enter the value of a:")
    a=int(a)
    result=a*a
    print(f"result:{result}")
except ValueError:
    print(f"string cannot be converted into integer")
