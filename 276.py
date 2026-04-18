#list
#insert an element at a specific index.
#method 1)
a=list(map(int,input("enter elements:").split()))
x=int(input("enter the index:"))
val=int(input("enter the value:"))
a.insert(x,val)
print(a)
