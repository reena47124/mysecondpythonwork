#check if an array is a palindrome.
import array
nums=list(map(int,input("enter the elements:").split()))
arr=array.array('i',nums)
n=len(arr)
rev=array.array('i')
for i in range(n-1,-1,-1):
    rev.append(arr[i])
is_palindrome=True
for i in range(n):
    if arr[i]!=rev[i]:
        is_palindrome=False
        break
if is_palindrome:
    print(f"{arr} is a palindrome.")
else:
    print(f"{arr} is not a palindrome.")                      