#Write a lambda function to check if a number is divisible by 3 and 5.
check=lambda num:"divisible" if num%3==0 and num%5==0 else "not divisible"
print(check(12))
print(check(15))
