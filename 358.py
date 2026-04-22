#dictionary
#sort a dictionary by keys.
d={'a':1,'c':2,'d':5,'f':0,'e':78,'l':34}
keys=list(d.keys())
n=len(keys)
for i in range(n):
    for j in range(i+1,n):
        if keys[i]>keys[j]:
            keys[i],keys[j]=keys[j],keys[i]
sorted_d={}
for key in keys:
    sorted_d[key]=d[key]
print(sorted_d)
                