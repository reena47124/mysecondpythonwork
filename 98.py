#find square root and floor of an integer.
#method 1)using **0.5
num=int(input("enter the number:"))
root=int(num**0.5)
if root*root==num:
    print(f"{num} is perfect square with root {root}")
else:
    print(f"{num} is not a perfect square,its floor value is {root}")    
     