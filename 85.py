#find GCD or HCF of two numbers.
#method 2) euclidean method.
a,b=map(int,input("enter two numbers:").split())
while b!=0:
    a,b=b,a%b   #order of numbers dont matter.
print(f"HCF of two given numbers is {a}")
