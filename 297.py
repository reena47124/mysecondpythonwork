#list
#find the subarray with maximum sum.
#method 1)brute force
a=list(map(int,input("enter elements:").split()))
n=len(a)
max_sum=float('-inf')
start=end=0
for i in range(n):
    current_sum=0
    for j in range(i,n):
        current_sum+=a[j]
        if max_sum<current_sum:
            max_sum=current_sum
            start=i
            end=j
print(f"maximum sum:{max_sum}")
print(a[start:end+1])            
           

