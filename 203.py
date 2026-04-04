#count how many times a number appears in the array.
import array
a=array.array('i',[1,2,3,2,4,2,5,2,2])
target=2
count=0
for i in a:
    if i==target:
        count+=1
print(f"{target} appears total {count} times.")
        