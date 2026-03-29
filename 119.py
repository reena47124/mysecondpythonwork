#Write a function that returns the sum of all elements in a list.
def func_sum(lst):
    sum=0
    for i in lst:
        sum=sum+i
    print(f"sum of all elements in the list is {sum}")
    return sum
print(func_sum([1,4,6,2,9]))        