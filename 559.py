#find gcd
a = 24
b = 36
while b != 0:
    a, b = b, a % b
print(a)