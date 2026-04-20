#tuple
#find the 2nd largest element.
#method 3)
t=tuple(map(int,input("enter elements:").split()))
t1=tuple(set(t))
l1=list(t1)
first=second=float('-inf')
for num in l1:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(f"2nd largest:{second}")
            