#sets
#check if two lists have any common elements.
l1=list(map(int,input("enter the elements of the first list:").split()))
l2=list(map(int,input("enter the elements of the second list:").split()))
s1=set(l1)
s2=set(l2)
is_present=False
for item in s1:
    if item in s2:
        is_present=True
        break
if is_present:
    print(f"yes")
else:
    print(f"no")
