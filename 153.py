#Write a recursive function to calculate sum of first N natural numbers.
def func_sum(n):
    if n==0:
        return 0
    return n+func_sum(n-1)
print(func_sum(5))
print(func_sum(7))    