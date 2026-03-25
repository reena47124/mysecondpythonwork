#sum of digits of a number.
num=int(input("enter the digit:"))
count=0
while num!=0:
    digit=num%10
    count=count+digit
    num=num//10
print(f"{count} is sum of the digits of a given number.")    
