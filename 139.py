#Write a function to reverse a number.
def func_rev(num):
    temp=num
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print(f"{rev} is the reverse of number {temp}.")
    return rev
func_rev(987632)
