#check if a number is palindrome or not.
num=int(input("enter the number:"))
temp=num
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==temp:
    print(f"{temp} is a palindrome.")
else:
    print(f"{temp} is not a palindrome.")

