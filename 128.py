#Write a function to find the largest among three numbers.
def func_larger(num1,num2,num3):
    if (num1>num2 and num1>num3):
        print(f"{num1} is largest among three numbers.")
    elif (num2>num1 and num2>num3):
        print(f"{num2} is largets among three numbers.")
    else:
        print(f"{num3} is the largets among three numbers.")
    return
func_larger(12,23,87) 
func_larger(14,43,23)           