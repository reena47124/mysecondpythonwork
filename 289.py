#list
#find the union of two lists.
#method 1)
a=list(map(int,input("enter elements of first list:").split()))
b=list(map(int,input("enter elements of second list:").split()))
a=set(a)
b=set(b)
result=list(a|b)
print(result)
