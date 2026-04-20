#tuple
#merge two tuples and remove duplicates.
t1=tuple(map(int,input("enter elements of 1st tuple:").split()))
t2=tuple(map(int,input("enter elements of 2nd tuple:").split()))
l1=list(t1)
l2=list(t2)
for num in l1:
    l2.append(num)
l2=list(set(l2))
t3=tuple(l2)
print(t3)
    