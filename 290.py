#list
#find the union of two lists.
#method 1)
a=list(map(int,input("enter elements of first list:").split()))
b=list(map(int,input("enter elements of second list:").split()))
for num in b:
    if num not in a:
        a.append(num)
print(a)
        