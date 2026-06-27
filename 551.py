#bineary search
nums = [2, 5, 8, 12, 15, 18, 20]
target = 15
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print("Found at index", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
