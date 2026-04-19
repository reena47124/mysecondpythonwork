#list
#find all subarray with given sum.
#method 1)brute force.
a=list(map(int,input("enter elements:").split()))
k=int(input("enter value of k:"))
n=len(a)
for i in range(n):
    sum=0
    for j in range(i,n):
        sum=sum+a[j]
        if sum==k:
            print(a[i:j+1])
            

