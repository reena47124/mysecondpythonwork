#find the second largest
a = [10, 40, 20, 60, 30]
largest = second = float('-inf')
for num in a:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(second)