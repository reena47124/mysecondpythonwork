#list
#reverse a list without using built-in method.
a=list(input("enter elements:").split())
b=[]
n=len(a)
for i in range(n-1,-1,-1):
    b.append(a[i])
print(b)

