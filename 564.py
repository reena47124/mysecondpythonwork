#move all zeros to the end.
def move_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr
arr = [8,0,5,0,10,0]
print(move_zeros(arr))