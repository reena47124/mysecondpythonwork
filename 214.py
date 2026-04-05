#shift all elements one position to the right.
import array
a=array.array('i',[1,2,3,4,5,6,7])
n=len(a)
temp=a[n-1]
for i in range(n-1,0,-1):
    a[i]=a[i-1]
a[0]=temp
print(a)
