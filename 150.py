#Write a function to count how many prime numbers exist till N.
def func_prime(n):
    count=0
    for num in range(2,n+1):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num,end=",")
            count+=1
    print()        
    print(f"there are {count} prime numbers till {n}.")
    return count
func_prime(18)            