#find the 2nd largest number in an array.
import array
a=array.array('i',[12,34,23,67,90,89])
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
a.remove(maximum)
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
print(f"2nd largest number from the given array is:{maximum}")                