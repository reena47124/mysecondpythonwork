#Write a function to check if a number is a multiple of both 3 and 7.
def func_check(num):
    if (num%3==0 and num%7==0):
        print(f"{num} is a multiple of both 3 and 7.")
    else:
        print(f"{num} is not a multiple of both 3 and 7.") 
    return
func_check(21)
func_check(35)
func_check(49)       