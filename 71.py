#multiplication table.
num=int(input("enter the number:"))
print("multiplication of given number is:",end=" ")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
