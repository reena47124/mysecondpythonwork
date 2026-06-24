#practice
a = [1,2,3,4]
b = [3,4,5,6]
common = []
for num in a:
    if num in b:
        common.append(num)
print(common)