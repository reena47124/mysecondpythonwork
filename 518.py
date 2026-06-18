#find the largest element.
a = [12, 45, 7, 89, 34]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)