#Write a function to calculate factorial of a number.
def func_fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"factorial of a given number is {fact}")
    return fact 
func_fact(6)
   