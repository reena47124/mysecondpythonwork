#invert a dictionary
d = {'a':1,'b':2}
new_d = {}
for key, value in d.items():
    new_d[value] = key
print(new_d)