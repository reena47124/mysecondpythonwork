#find diagonal sum of a matrix
m=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in range(len(m)):
    sum+=m[i][i]
print(sum)    