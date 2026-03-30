#Write a function that returns nth term of Fibonacci series.
def func_fibo(n):
    a=0
    b=1
    if n==1:
        print(f"1st term of fibonacci series is 0")
        return[0]
    if n==2:
        print(f"2nd term of fibonacci series is 1")
        return[1]
    for i in range(3,n+1):
        a,b=b,a+b
    print(f"{n}th term of fibonacci series is {b}")
    return b
func_fibo(1)
func_fibo(2)
func_fibo(3)
func_fibo(5)
func_fibo(7)
    