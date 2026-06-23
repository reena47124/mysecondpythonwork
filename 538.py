#sum of all elements of a matrix
m=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for row in m:
    for num in row:
        sum+=num
print(sum)        