#armstrong number or not.
num=int(input("enter the number:"))
temp=num
x=0
while temp!=0:
    temp=temp//10
    x+=1
count=0
temp=num  #re-assign temp's value further.
while temp!=0:
    digit=temp%10
    count=count+(digit**x)
    temp=temp//10   
if count==num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")            