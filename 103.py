#kth digit in 'a' raised to power 'b'.
a,b,k=map(int,input("enter values of a,b,k respectively:").split())
num=a**b
for i in range(1,k):
    num=num//10
digit=num%10    
print(f"{k}th digit of a raised to power b is {digit}")   

