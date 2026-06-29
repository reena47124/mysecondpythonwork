#find lcm
a = 12
b = 18
greater = max(a, b)
while True:
    if greater % a == 0 and greater % b == 0:
        print(greater)
        break
    greater += 1