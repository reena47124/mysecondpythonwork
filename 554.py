#flatten a nested list
a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
b=[]
for sublist in a:
    for num in sublist:
        b.append(num)
print(b)        