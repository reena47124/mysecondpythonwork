#nth fibonacci number.
n=int(input("enter the value of n:"))
a=0
b=1
if n==1:
    print(f"{n}th term is {a}")
elif n==2:
    print(f"{n}th term is {b}")
else:
    for i in range(0,n-2):
        a,b=b,a+b
    print(f"{n}th term is {b}") 
       



