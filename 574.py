#decimal to binary
num=12
binary=""
while num>0:
    binary=str(num%2)+binary
    num//=2
print(binary)