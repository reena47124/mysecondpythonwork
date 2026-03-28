#print all prime numbers between 1 to 100.
print("all prime numbers between 1 to 100 are:",end=" ")
for num in range(2,101):
    is_prime=True
    for i in range(2,num): #this loop will not run for 2, hence 2 remain prime number.
        if num%i==0:
            is_prime=False
            break
    if is_prime:
            print(num,end=",")    
    