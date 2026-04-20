#tuple
#find the 2nd largest element.
#method 2)
t=tuple(map(int,input("enter elements:").split()))
t1=tuple(set(t))
l1=list(t1)
n=len(l1)
largest=l1[0]
for i in range(n):
    if l1[i]>largest:
        largest=l1[i]
l1.remove(largest) 
largest=l1[0]
for i in range(n-1):
    if l1[i]>largest:
        largest=l1[i]
print(f"2nd largest:{largest}")
               
