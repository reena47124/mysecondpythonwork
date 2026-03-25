#sum of digits of a number.
num=int(input("enter the number:"))
count=0
while num!=0:
    digit=num%10
    count=count+digit
    num=num//10
print("sum of digits of a number is:",count)    