#Write a function to check if a number is divisible by 5 and 11.
def func_check(num):
    if (num%5==0 and num%11==0):
        print(f"{num} is divisible by both 5 and 11.")
    else:
        print(f"{num} is not divisible by both 5 and 11.")
    return
func_check(55)
func_check(21)

