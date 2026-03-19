#count number of digits in a number using loop.
num=int(input("enter the number:"))
count=0
while num!=0:
    num=num//10
    count+=1
print(f"the number of digit in given number is {count}")
