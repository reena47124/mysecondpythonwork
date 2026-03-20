#print fibonacci series uo to n terms.
n=int(input("enter the term upto which you want to print the fibonacci series:"))
a=0
b=1
print("fibonacci series is:",end=" ")
for i in range(n):
    print(a,end=",")
    a,b=b,a+b
print()
