#find LCM of two numbers.
#method 2) euclidean method.
a,b=map(int,input("enter two numbers:").split())
c,d=a,b #store original values
while b!=0:
    a,b=b,a%b
hcf=a
lcm=(c*d)/hcf 
print(f"lcm of two given numbers is {lcm}")
