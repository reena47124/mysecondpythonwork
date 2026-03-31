#Write a function to find GCD of two numbers.
def func_gcd(a,b):
    while b!=0:
        a,b=b,a%b
    print(f"gcd={a}")
    return(a)
func_gcd(36,60)
func_gcd(24,86)
