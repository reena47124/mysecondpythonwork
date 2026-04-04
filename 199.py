#Write a program to find sum of all elements in an array.
import array
a=array.array('i',[12,34,78,36,98])
sum=0
for i in a:
    sum=sum+i
print(f"sum:{sum}")
    