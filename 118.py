#Write a function that takes a list and returns its length (without using len()).
def func_length(lst):
    count=0
    for i in lst:
        count+=1
    print(f"length of the given list is {count}")
    return count
print(func_length([1,2,3,4,5,6,7,8,4,3]))    

     
