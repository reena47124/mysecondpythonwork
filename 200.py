#Write a program to find maximum and minimum element in an array.
import array
a=array.array('i',[1,2,3,4,5])
maximum=a[0] 
for i in a:
    if i>maximum:
        maximum=i
print(f"maximum is:{maximum}")
minimum=a[0]
for i in a:
    if i<minimum:
        minimum=i
print(f"minimum is:{minimum}")                                  