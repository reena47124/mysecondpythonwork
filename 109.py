#modular exponentiation.
x,n,m=map(int,input("enter the values of x,n,m respectively:").split())
num=x**n
result=num%m
print(f"{result} is the modular exponent of {x} raised to the power {n}.")
