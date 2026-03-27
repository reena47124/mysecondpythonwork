#pair cube count.
n=int(input("enter value of n:"))
count=0
for a in range(n+1):
    for b in range(n+1):
        if a**3+b**3==n:
            count+=1
print(count)
            