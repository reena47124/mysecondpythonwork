#dictionary
#how to take a dictionary input from the user.
#method 1)
d={}
n=int(input("enter the number of elements:"))
for i in range(n):
    key=int(input("enter the value of keys:"))
    value=input("enter the values of value:")
    d[key]=value
print(d)
