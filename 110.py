#program for nth catalan number.
n=int(input("enter the value of n:"))
fact1=1
fact2=1
fact3=1
for i in range(1,2*n+1):
    fact1=fact1*i
for i in range(1,n+2):
    fact2=fact2*i
for i in range(1,n+1):
    fact3=fact3*i
mul=fact2*fact3
result=fact1//mul
print(f"{n}th catalan number is {result}.")            
