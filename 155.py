#Write a recursive function to count digits in a number.
def func_count(num):
    if num==0:
        return 0
    return 1+func_count(num//10)
print(func_count(23418))