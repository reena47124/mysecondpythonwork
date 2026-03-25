#reverse a number using loop.
num=int(input("enter a number you want to reverse:"))
rev=0
while num!=0:
    digit=num%10  #get last digit
    rev=rev*10+digit
    num=num//10   #remove last digit
print(f"reverse of given number is:{rev}")    