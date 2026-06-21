#move all zeros to the end,optimize method,two-pointer technique.
a=[1,0,0,0,5,0,7]
pos=0
for i in range(len(a)):
    if a[i]!=0:
        a[pos],a[i]=a[i],a[pos]
        pos+=1
print(a)        