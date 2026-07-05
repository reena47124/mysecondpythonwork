#find second largest number.
def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second
arr = [10,5,8,20,15]
print(second_largest(arr))