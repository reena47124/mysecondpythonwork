#sort an array without using sort() method.
import array
a=array.array('i',[2,45,12,0,56,4,1,40,2])
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
