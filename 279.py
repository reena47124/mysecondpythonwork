#list
#insert an element at a specific index.
#method 2)
a=list(map(int,input("enter elements:").split()))
index=int(input("enter the index:"))
value=int(input("enter the value:"))
a.append(0)   #increase length of the list
n=len(a)
for i in range(n-1,index,-1):
    a[i]=a[i-1]
a[index]=value
print(a)
    