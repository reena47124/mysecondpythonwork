#rotate an array by k position to right.
import array
a=array.array('i',[1,2,3,4,5,6,7])
k=int(input("enter value of k:"))
n=len(a)
for i in range(k):
    temp=a[n-1]
    for j in range(n-1,0,-1):
        a[j]=a[j-1]
    a[0]=temp
print(a) 
