#move all zeros to the end,bult-in method
a=[1,0,3,0,5,0,7]
nums=[]
zeros=[]
for i in range(len(a)):
    if a[i]==0:
        zeros.append(a[i])
    else:
        nums.append(a[i])
for i in range(len(zeros)):
    nums.append(zeros[i]) 
print(nums)               