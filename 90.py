#find whether a given positive integer n is perfect or not.
n=int(input("enter the number:"))
count=0
#for i in range(1,n):
for i in range(1,n//2+1):   #for optimization
    if n%i==0:
        count=count+i
if count==n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")            