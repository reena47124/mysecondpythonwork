#find the intersection of 2 arrays.
#method: with the help of set
import array
a=array.array('i',[1,2,3,4,5])
b=array.array('i',[3,4,5,6,7])
result=(set(a)&set(b))
print(f"intersection of 2 given arrays is:{result}")
