#list
#rotate a list by k-position right.
a=list(map(int,input("enter the elements:").split()))
k=int(input("enter the value of k:"))
n=len(a)
for i in range(k):
    temp=a[n-1]
    for j in range(n-1,0,-1):
        a[j]=a[j-1]
    a[0]=temp
print(a)
        
