#find the union of 2 arrays.
#method:without duplicates.
import array
a=array.array('i',[1,2,3,4,5])
b=array.array('i',[3,4,5,6,7])
for i in b:
    if i not in a:
        a.append(i)
print(f"union of 2 given arrays is:{a}")        