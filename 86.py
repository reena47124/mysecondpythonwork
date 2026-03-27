#find GCD or HCF of two numbers.
#method 3) loop method.
a,b=map(int,input("enter two numbers:").split())
HCF=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        HCF=i
print(f"HCF of two given number is {HCF}")
        