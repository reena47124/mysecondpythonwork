#Write a function with a default argument (e.g., default value of b = 10) and test different cases.
def func_check(a,b=10):
    mul=a*b
    print(mul)
    return mul
func_check(8) #default argument
func_check(12,9)  #positional argument
func_check(a=10,b=12)  #keyword argument
func_check(23,b=2)

