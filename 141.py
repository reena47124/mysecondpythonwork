#Write a function to find sum of digits of a number.
def func_sum(num):
    sum=0
    while num!=0:
        digit=num%10
        sum=sum+digit
        num=num//10
    print(f"sum of the digits of a given number is {sum}")
    return sum
func_sum(12367)    