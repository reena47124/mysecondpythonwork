#check if a number is a power of another number or not.
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
for i in range(100):
    if x**i==y:
        print(f"{y} is {i}th power of {x}")
        break
else:
    print(f"{y} is not the power of {x}")
