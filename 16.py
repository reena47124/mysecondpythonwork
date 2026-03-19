#find the largest of 3 numbers.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and num1>num3:
    print(f"first number that is,{num1} is largest.")
elif num2>num1 and num2>num3:
    print(f"second number that is,{num2} is largest.")
else:
    print(f"third number that is,{num3} is largest.")


