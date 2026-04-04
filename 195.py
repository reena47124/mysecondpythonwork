#Write a program to access and print elements using index.
import array
b=array.array('i',[1,2,3,4,5])
for i in range(len(b)):
    print(f"{i} index element of the array is:{b[i]}")
