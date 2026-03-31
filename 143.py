#Write a function to print all prime numbers up to N.
def func_prime(n):
    print(f"all prime numbers up to {n} are:")
    for num in range(2,n+1):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num,end=",")
    return
func_prime(17)        