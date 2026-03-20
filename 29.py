#find factorial of a number.
n=int(input("enter the number you want to find factorial of:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} is {fact}")
    