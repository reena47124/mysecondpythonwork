#check if a number is palindrome.
num=int(input("enter the number:"))
org=num
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if org==rev:
    print(f"{org} is a palindrome.")
else:
    print(f"{org} is not a palindrome.") 
