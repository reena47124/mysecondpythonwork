#rotate an array by k position to left.
import array
a=array.array('i',[1,2,3,4,5,6,7])
k=int(input("enter the value of k:"))
n=len(a)
for i in range(k):
    temp=a[0]
    for j in range(n-1):
        a[j]=a[j+1]
    a[n-1]=temp
print(a) 
       