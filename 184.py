#Write a function that takes 3 arguments and returns the maximum.
def func_max(num1,num2,num3):
    if num1>num2 and num1>num3:
        maximum=num1
        print(f"{num1} is muximum.")
    elif num2>num1 and num2>num3:
        maximum=num2
        print(f"{num2} is maximum.")
    else:
        maximum=num3
        print(f"{num3} is maximum")
    return maximum
func_max(23,90,45)
