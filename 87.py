#find LCM of two numbers.
#method 1) built-in method.
import math
a,b=map(int,input("enter two numbers:").split())
HCF=math.gcd(a,b)
LCM=(a*b)/HCF
print(f"LCM of two given numbers is {LCM}")