#Write a recursive function to find sum of digits of a number.
def func_sum(num):
    if num==0:
        return 0
    return num%10+func_sum(num//10)
print(func_sum(2345))