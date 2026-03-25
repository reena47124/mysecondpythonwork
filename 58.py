#count digit in a number.
num=int(input("enter number:"))
count=0
while num!=0:
    digit=num%10  #get first digit
    count=count+1
    num=num//10
print(f"total digit in the given number if:{count}")    