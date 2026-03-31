#Write a function to find LCM of two numbers.
def func_lcm(a,b):
    mul=a*b
    while b!=0:
        a,b=b,a%b
    gcd=a
    lcm=mul//gcd
    print(f"lcm={lcm}")
    return lcm
func_lcm(36,60)   