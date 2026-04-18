#list
#find the intersection of two lists.
#method 2)
a=list(map(int,input("enter elements of first list:").split()))
b=list(map(int,input("enter elements of second list:").split()))
c=[]
for num in a:
    if num in b and num not in c:
        c.append(num)
print(c)
