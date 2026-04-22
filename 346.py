#dictionary
#merge two dictionaries.
d1={1:"apple",2:"mango",3:"banana"}
d2={'a':"hi",'b':"there"}
for key,value in d2.items():
    d1[key]=value
print(d1)
