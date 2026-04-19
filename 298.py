#list
#find the maximum product subarray.
#method 1)brute force
a=list(map(int,input("enter elements:").split()))
n=len(a)
max_product=float('-inf')
start=end=0
for i in range(n):
    current_product=1
    for j in range(i,n):
        current_product*=a[j]
        if max_product<current_product:
            max_product=current_product
            start=i
            end=j
print(f"maximum product:{max_product}")
print(a[start:end+1])
            