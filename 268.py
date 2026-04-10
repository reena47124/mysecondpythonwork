#leetcode(1)
#given an array of integers nums and an integer target,return indices of the two numbers such that they add up to target.
#nums=list(map(int,input("enter elements of the array:").split()))
#target=int(input("enter the value of the target:"))
nums=[2,7,11,15]
target=9
n=len(nums)
for i in range(n):
    for j in range(i+1,n-1):
        if nums[i]+nums[j]==target:
            print(i,j)
            