#list
#find the missing number from 1 to n.
n=int(input("enter the value of n:"))
a=list(map(int,input(f"enter value from 1 to {n} with one missing element:").split()))
n=len(a)+1
expected_sum=n*(n+1)//2
actual_sum=0
for num in a:
    actual_sum+=num
missing_element=expected_sum-actual_sum
print(f"missing element is:{missing_element}")



