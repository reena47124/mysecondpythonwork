#sets
#find unique elements from two lists combined.
l1=list(map(int,input("enter the elements of the first list:").split()))
l2=list(map(int,input("enter the elements of the second list:").split()))
for item in l2:
    if item not in l1:
        l1.append(item)
s=set(l1)
print(s)
        

