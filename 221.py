#find the intersection of 2 arrays.
#method: with duplicates
import array
a=array.array('i',[1,2,3,4,5,1,3])
b=array.array('i',[3,4,5,6,7])
c=array.array('i')
for i in a:
    if i in b:
        c.append(i)
print(f"intersection of 2 given arrays is:{c}")

