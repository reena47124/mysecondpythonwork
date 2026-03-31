#Write a function to check if a number is Armstrong.
def func_arm(num):
    temp=num
    count=0
    while temp!=0:
        digit=temp%10
        count+=1
        temp=temp//10
    temp=num 
    sum=0
    while temp!=0:
        digit=temp%10
        sum=sum+digit**count
        temp=temp//10
    if sum==num:
        print(f"the {num} is an armstrong number.")
    else:
        print(f"the {num} is not an armstrong number.")
    return
func_arm(9474)
func_arm(150)               