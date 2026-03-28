#find square root and floor of an integer.
#method 2) loop method
num=int(input("enter the number:"))
root=0
for i in range(1,num+1):
    if i*i<=num:
        root=i       
if root*root==num:
    print(f"{num} is perfect square, and its root value is {root}")
else:
    print(f"{num} is not a perfect square, and its floor value is {root}")                        