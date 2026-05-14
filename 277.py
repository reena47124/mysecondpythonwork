#list
#delete an element from a list.
#method 1)
a=list(map(int,input("enter elements:").split()))
val=int(input("enter the element you want to delete:"))
a.remove(val)
print(a)

