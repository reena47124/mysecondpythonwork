#check array is sorted or not
a = [1, 2, 3, 4, 5]
sorted_array = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        sorted_array = False
        break
print(sorted_array)