#Write a function to check if a number is palindrome.
def func_pali(num):
    temp=num
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if rev==temp:
        print(f"{temp} is palindrome.")
    else:
        print(f"{temp} is not a palindrome.")  
    return
func_pali(1234321)
func_pali(1765)          
