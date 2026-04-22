#dictionary
#invert a dictionary i.e. swap keys and values.
d={1:"apple",2:"banana",3:"mango",4:"cherry",5:"apricot"}
d1={}
for key,value in d.items():
    d1[value]=key
print(d1)
