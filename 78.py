#reverse the given digit.
num=int(input("enter the digit:"))
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(f"{rev} is the reverse of a given digit.")
    