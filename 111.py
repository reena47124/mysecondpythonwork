#binomial coefficient.
n,k=map(int,input("enter the values of n anf k respectively:").split())
fact1=1
fact2=1
fact3=1
if k>n:
    print(f"invalid input!")
else: 
    for i in range(1,n+1):
        fact1=fact1*i
    for i in range(1,k+1):
        fact2=fact2*i
    for i in range(1,(n-k)+1):
         fact3=fact3*i   
    mul=fact2*fact3
    result=fact1//mul
    print(f"binomial coefficient is {result}.")            