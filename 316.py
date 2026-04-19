#tuple
#check if a tuple is palindrome.
t=tuple(map(int,input("enter elements:").split()))
rev=t[::-1]
n=len(t)
is_palindrome=True
for i in range(n):
    if t[i]!=rev[i]:
        is_palindrome=False
        break
if is_palindrome:
    print(f"tuple is palindrome")
else:
    print(f"tuple is not a palindrome")
            