#program to calculate the value of nPr.
n,r=map(int,input("enter values of n and r respectively:").split())
s=n-r
factn=1
facts=1
for i in range(1,n+1):
    factn=factn*i
for i in range(1,s+1):
    facts=facts*i
result=factn//facts
print(f"nPr is {result}.")        