#Write a function to find the maximum of two numbers.
def func_max(num1,num2):
    if num1>num2:
        print(f"{num1} is greater.")
        return num1
    else:
        print(f"{num2} is greater.")
        return num2
print(func_max(23,43))

