#write a recursive function to find sum of squares of first n numbers.
def func_sum(n,i=1,sum=0):
    if i>n:
        return sum
    return func_sum(n,i+1,sum+i*i)
print(func_sum(4))
print(func_sum(5))


    