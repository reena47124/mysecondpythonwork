#tuple
#sort a tuple.
t=tuple(map(int,input("enter elements:").split()))
li=list(t)
n=len(t)
for i in range(n-1):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]

t1=tuple(li)
print(t1)
