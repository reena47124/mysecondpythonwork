#practice
#find missing number in a series
nums = [1,2,3,5]
n = 5
missing = n*(n+1)//2 - sum(nums)
print(missing)