#merge two arrays into one.
import array
a=array.array('i',[1,2,3,4,5]) 
b=array.array('i',[6,7,8,9,10])
for i in b:
    a.append(i)
print(a)
         