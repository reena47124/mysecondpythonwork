#count numbers with exactly 3 divisors.
#method 2) optimize solution
num=int(input("enter the number:"))
count=0
for i in range(2,int(num**0.5)+1):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        square=i*i
        if square<=num:
            print(square)
            count+=1
print(f"there is {count} numbers with exactly 3 divisors.")            

