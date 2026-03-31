#Write a recursive function to find Nth Fibonacci number.
def func_fibo(n):
    if n==0:
        return 0
    if n==1:
        return 0
    if n==2:
        return 1
    return func_fibo(n-1)+func_fibo(n-2)
print(func_fibo(7))
