#dictionary
#remove duplicate values from a dictionary.
d={1:"apple",2:"banana",3:"mango",4:"apple",5:"mango"}
d1={}
seen=set()
for key,value in d.items():
    if value not in seen:
        d1[key]=value
        seen.add(value)
print(d1)
        
