#Use lambda with map() to square numbers from 1 to N.
n=int(input("enter value of n:"))
num=list(range(1,n+1))
square=list(map(lambda x:x*x,num))
print(square)
