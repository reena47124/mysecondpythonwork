#Write a recursive function to check if a number is palindrome.
def func_rev(num,rev=0):
    if num==0:
        return rev
    return func_rev(num//10,rev*10+num%10)
def func_pali(num):
    return num==func_rev(num)
print(func_pali(121))
print(func_pali(123))