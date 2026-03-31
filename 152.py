#Write a recursive function to print numbers from 1 to N.
def func_print(n):
    if n==0:
        return
    else:
        func_print(n-1)
        print(n,end=",")
func_print(8)    