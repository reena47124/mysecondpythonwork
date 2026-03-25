#sum of squares of first n natural numbers.
n=int(input("enter the value of n:"))
count=0
print("sum of squares of first n natural numbers is:",end=" ")
for i in range(1,n+1):
    count=count+(i*i)
print(count)
    