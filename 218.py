#find the missing number in an array of 1 to n.
import array
a=array.array('i',[1,2,3,5,6,7])
n=7
expected_sum=n*(n+1)//2
actual_sum=0
for i in a:
    actual_sum+=i
missing=expected_sum-actual_sum
print(f"missing term is:{missing}")
    
