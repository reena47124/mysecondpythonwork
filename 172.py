#Write a lambda function to check if a number is positive, negative, or zero.
check=lambda num:"positive" if num>0 else("negative" if num<0 else "zero")
print(check(-9))
print(check(0))
print(check(7))
