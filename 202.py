#check whether a given element exists in the array.
import array
a=array.array('i',[1,2,3,4,5])
target=8
for i in a:
    if i==target:
        print(f"element exists!")
        break
else:
    print(f"element doesnt exist.")