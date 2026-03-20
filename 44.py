#swap two numbers without using a third variable.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num1,num2=num2,num1
print(f"numbers after swapping are: num1={num1}, num2={num2}")