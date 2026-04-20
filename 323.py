#tuple
#find common elements between two tuples.
t1=tuple(map(int,input("enter elements of 1st tuple:").split()))
t2=tuple(map(int,input("enter elements of 2nd tuple:").split()))
t3=set(t1)
t4=set(t2)
result=tuple(t3&t4)
print(result)
