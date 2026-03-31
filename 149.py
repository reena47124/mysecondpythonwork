#Write a function to print Fibonacci series up to N terms.
def func_fibo(n):
    fib=[]
    a=0
    b=1
    if n<=0:
        return
    if n==1:
        fib.append(a)
    else:
        fib=[0,1]
        for i in range(3,n+1):  #this loop will not run i=2,for i=2 fib=[0,1]
             a,b=b,a+b
             fib.append(b)
    print(f"fibonacci series of {n} terms is {fib}")
    return fib    
func_fibo(8)
func_fibo(0)
func_fibo(1)
func_fibo(2)
func_fibo(3)
