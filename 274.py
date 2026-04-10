#list
#sort a list without using sort().ascending order
a=list(map(int,input("enter elements of list:").split()))
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(f"sorted list:{a}")
