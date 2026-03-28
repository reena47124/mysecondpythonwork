#program to calculate value of nCr.
n,r=map(int,input("enter the values of n and r respectively:").split())
s=n-r
factn=1
facts=1
factr=1
for i in range(1,n+1):
    factn=factn*i
for i in range(1,s+1):
    facts=facts*i
for i in range(1,r+1):
    factr=factr*i 
mul=facts*factr
result=factn//mul
print(f"nCr is {result}")          