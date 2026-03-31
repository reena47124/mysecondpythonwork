#Write a recursive function to calculate factorial of a number.
def func_fact(n):
    if n==0:
        return 1
    return n*func_fact(n-1)
print(func_fact(5))
print(func_fact(6))
