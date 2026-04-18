#list
#delete an element from a list.
#method 2)
a=list(map(int,input("enter elements:").split()))
val=int(input("enter the element you want to delete:"))
if val in a:
    a.remove(val)
else:
    print(f"value not found in the list!")
print(a)
        