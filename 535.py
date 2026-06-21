#move all zeros to the end,optimize method
a=[1,0,0,0,5,0,7]
n=len(a)
i=0
while i<n:
    if a[i]==0:
        for j in range(i+1,n):
            a[j-1]=a[j]
        a[n-1]=0
        n-=1
    else:
        i+=1        
print(a)           
