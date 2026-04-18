#list
#rotate a list by k-position left.
a=list(map(int,input("enter elements:").split()))
k=int(input("enter the value of k:"))
n=len(a)
for i in range(k):
    temp=a[0]
    for j in range(n-1):
        a[j]=a[j+1]
    a[n-1]=temp
print(a)        