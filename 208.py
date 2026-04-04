#remove duplicate elements from an array.
import array
a=array.array('i',[1,2,3,1,2,3,4,5,6,1,2])
new=array.array('i')
for i in a:
    if i not in new:
        new.append(i)
print(new)                  