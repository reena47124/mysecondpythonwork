#sets
#find missing elements between two lists.
l1=list(map(int,input("enter the elements of the first list:").split()))
l2=list(map(int,input("enter the elements of the second list:").split()))
s=set()
for item in l1:
    if item not in l2:
        s.add(item)
for item in l2:
    if item not in l1:
        s.add(item)
print(s)
        
