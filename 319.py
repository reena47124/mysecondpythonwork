#tuple
#remove duplicates from a tuple.
t=tuple(map(int,input("enter elements:").split()))
li=list(t)
a=[]
for num in li:
    if num not in a:
        a.append(num)
b=tuple(a)
print(b)
        
