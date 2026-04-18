#list
#create a list of squares of numbers.
a=list(map(int,input("enter elements:").split()))
squares=[]
for num in a:
    squares.append(num*num)
print(squares)
    