#Write a function using *args to sum all numbers passed.
def func_sum(*args):
    sum=0
    for num in args:
        sum=sum+num
    print(sum) 
    return sum
func_sum(23,45,12,89)
func_sum(1,2,3,4,5,6,7,8,9,10)   
