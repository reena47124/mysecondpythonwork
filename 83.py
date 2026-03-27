#factorial
n=int(input("enter value of n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of given number is {fact}")    
