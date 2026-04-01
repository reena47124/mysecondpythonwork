#Write a recursive function to check if a number is prime.
def is_prime(num,i=2):
    if num<=1:
        return False
    if num%i==0:
        return False
    if i>(int(num**0.5)):
        return True
    return is_prime(num,i+1)
print(is_prime(7,i=2))
print(is_prime(9,i=2))
