#copy elements from one array to another.
import array
a=array.array('i',[1,2,3,4,5])
b=array.array('i')
for i in a:
    b.append(i)
print(f"array a is:{a}")
print(f"array b is:{b}")
    