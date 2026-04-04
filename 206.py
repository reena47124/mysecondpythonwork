#find the sum of all elements in an array.
import array
a=array.array('i',[12,34,56,78,23])
sum=0
for i in a:
    sum=sum+i
print(f"sum of all elements of given array is:{sum}")
    