#Write a recursive function to print numbers from n to 1.
def func_print(n):
    if n==0:
        return
    else:
        print(n,end=",")    
    return func_print(n-1)
func_print(7)    