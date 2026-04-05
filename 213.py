#shift all elements one position to the left.
import array
a=array.array('i',[1,2,3,4,5,6,7])
temp=a[0]
for i in range(len(a)-1):
    a[i]=a[i+1]
a[len(a)-1]=temp
print(a) 
