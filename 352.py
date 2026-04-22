#dictionary
#create a dictionary from two lits(keys+values).
keys=list(map(int,input("enter keys:").split()))
values=list(input("enter values:").split())
n=min(len(keys),len(values))
d={}
for i in range(n):
    d[keys[i]]=values[i]
print(d)
    

