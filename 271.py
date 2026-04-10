#list
#remove duplicates from a list.
#method 1)
a=list(map(int,input("enter the elements:").split()))
a=list(set(a))
print(a)
