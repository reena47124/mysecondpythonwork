#Write a function to calculate sum from 1 to N.
def func_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(f"sum is {sum}.")
    return sum
func_sum(10)
func_sum(7)
    