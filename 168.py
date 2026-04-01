#use lambda with filter() to get odd numbers.
num=[1,2,3,4,5,7]
odd=list(filter(lambda x:x%2!=0,num))
print(odd)