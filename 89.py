#find the LCM of two given numbers.
#method 3) loop method.
a,b=map(int,input("enter two numbers:").split())
HCF=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        HCF=i
lcm=(a*b)/HCF
print(f"lcm of two given numbers is {lcm}")
