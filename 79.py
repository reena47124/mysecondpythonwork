#check if the given number is prime or not.
num=int(input("enter the number:"))
if num<=1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2,num):   #this loop will not run for i=2
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

    