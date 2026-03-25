#given two integers n and m(m!=0).find the number closest to n and divisible by m.
n=int(input("enter value of n:"))
m=int(input("enter value of m:"))
found=False
for i in range(n):
    if (n-i)%m==0:
        print(f"{n-i} is the closest number to {n} divisible by {m}")
        found=True
        break

        