#find the sum of the two fractions and return the numerator and denominator of the result.
import math
a=list(map(int,input("enter the num and deno of first fraction:").split()))
b=list(map(int,input("enter the num and deno of second fraction:").split()))
x=a[0]*b[1]+a[1]*b[0]
y=a[1]*b[1]
GCD=math.gcd(x,y)
x1=x//GCD
y1=y//GCD
c=[]
c.append(x1)
c.append(y1)
print(f"sum of two fractions is:{c}")
