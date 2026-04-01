#Use lambda with filter() to get all even numbers from 1 to N.
n=int(input("enter the value of n:"))
num=list(range(1,n+1))
even_num=list(filter(lambda x:x%2==0,num))
print(even_num)
         