#tuple
#find the 2nd largest element.
#method 1)
t=tuple(map(int,input("enter elements:").split()))
t1=tuple(set(t))
l1=list(t1)
l1.sort()
print(f"second largest:{l1[-2]}")