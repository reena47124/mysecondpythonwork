#Write a program to take n inputs from user and store them in an array.
import array
n=int(input("enter the value of n:"))
a=array.array('i')
for i in range(n):
    num=int(input(f"enter {i+1} element:"))
    a.append(num)
print(f"array:{a}")    