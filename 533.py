#find all pairs with given sum
a=[1,2,3,4,5,6,7]
sum=7
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]==sum:
            print(a[i],a[j])
            