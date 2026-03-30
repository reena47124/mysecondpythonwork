#Write a function to check if a string is a palindrome.
def func_pali(s):
    rev=s[::-1]
    if rev==s:
        print(f"{s} is palindrome.")
    else:
        print(f"{s} is not s palindrome.") 
    return
func_pali("hello")
func_pali("abcdcba")    