#list
#check if a list is a palindrome or not.
a=list(map(int,input("enter elements:").split()))
rev=[]
n=len(a)
for i in range(n-1,-1,-1):
    rev.append(a[i])
is_palindrome=True
for i in range(n):
    if a[i]!=rev[i]:
        is_palindrome=False
        break
if is_palindrome:
    print(True)
else:
    print(False)

