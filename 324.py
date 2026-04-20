#tuple
#find common elements between two tuples.
#method 2)
t1=tuple(map(int,input("enter elements of 1st tuple:").split()))
t2=tuple(map(int,input("enter elements of 2nd tuple:").split()))
l1=list(t1)
l2=list(t2)
l3=[]
for num in l1:
    if num in l2 and num not in l3:
        l3.append(num)
result=tuple(l3)
print(result)
        