#tuple
#count occurrence of an element in a tuple.
t=tuple(map(int,input("enter elements:").split()))
target=int(input("enter target:"))
count=0
for item in t:
    if item==target:
        count+=1
print(count)
        