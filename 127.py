#write a function that returns fibonacci sequence upto n terms.
def func_fibo(n):
    a=0
    b=1
    fib=[]
    if n==1:
        fib.append(a)
        print(f"{n} sequence of the fibonacci series is {fib}.")
        return
    fib=[0]
    if n==2:
        fib.append(b)
        print(f"{n} sequence of the fibonacci series is {fib}.")
        return
    fib=[0,1]
    for i in range(3,n+1):
        a,b=b,a+b
        fib.append(b)
    print(f"{n} squence of the fibonacci series is {fib}")
    return
func_fibo(1)    
func_fibo(2)
func_fibo(3)    
func_fibo(5)
func_fibo(8)
func_fibo(11)