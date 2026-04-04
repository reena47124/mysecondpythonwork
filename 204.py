#reverse an array without using built-in methods.
import array
a=array.array('i',[1,2,3,4,5])
rev=array.array('i')
for i in range(len(a)-1,-1,-1):
    num=a[i]
    rev.append(num)
print(f"reverse of a given array is:{rev}")    