#dictionary
#sort a dictionary by values.
d={'a':1,'c':2,'d':5,'f':0,'e':78,'l':34}
sorted_d=dict(sorted(d.items(), key=lambda item:item[1]))
print(sorted_d)