#Write a recursive function to find GCD of two numbers (Euclidean method).
def func_gcd(a,b):
    if b==0:
        return a
    return func_gcd(b,a%b)
print(func_gcd(36,60))
print(func_gcd(36,48))