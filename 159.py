#Write a recursive function to calculate power (a^b) without using **.
def func_power(a,b):
    if b==0:
        return 1
    return a*func_power(a,b-1)
print(func_power(2,4))
print(func_power(5,3))
