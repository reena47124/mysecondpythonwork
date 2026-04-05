#move all zeros to the end of the array.
import array
a=array.array('i',[0,1,0,2,0,0,3,4,0,5])
b=array.array('i')
c=array.array('i')
n=len(a)
for i in range(n):
    if a[i]==0:
        c.append(a[i])
    else:
        b.append(a[i])
for i in c:
    b.append(i) 
print(b)               