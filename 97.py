#digital root of a given large integer.
num=int(input("enter the value of an integer:"))
while num>=10:
    temp=num
    sum=0
    while temp!=0:
        digit=temp%10
        sum=sum+digit
        temp=temp//10
    num=sum
print(f"{num} is digital root of given integer.")
              
       
            