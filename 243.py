#string.
#check if a string is a palindrome.
s=input("enter a string:")
n=len(s)
s1=s[::-1]
is_palindrome=True
for i in range(n):
    if s[i]!=s1[i]:
        is_palindrome=False
        break
if is_palindrome:
    print(f"palindrome!")
else:
    print(f"not a palindrome.")
            
