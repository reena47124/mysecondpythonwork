#practice
#second largest
nums = [12, 35, 1, 10, 34, 1]
largest = second = float('-inf')
for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)