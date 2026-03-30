#Write a function that returns absolute value without using abs().
def func_abs(num):
    if num<0:
        return -num
    else:
        return num
print(func_abs(-90))
print(func_abs(34))
