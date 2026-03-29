#find the largest prime factor of a given number.
n=int(input("enter the number:"))
a=[]
i=2
while i*i<=n:
    if n%i==0:
        a.append(i)
        while n%i==0:
            n=n//i
    i+=1
if n>1:
    print(f"{n} is the largest prime factor of a given number.")
else:
    print(f"{a[-1]} is the largest prime factor of a given number.")
                    