#find all even and odd numbers separately.
import array
a=array.array('i',[12,23,34,45,56,67,78,89,90,2,5,7,1,99])
e=array.array('i')
o=array.array('i')
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(f"all even numbers are:{e}")
print(f"all odd numbers are:{o}") 
