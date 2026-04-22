#dictionary
#find the key with maximum value.
d={1:23,2:34,3:12,4:78,5:35}
max_key=None
max_value=float('-inf')
for key,value in d.items():
    if value>max_value:
        max_value=value
        max_key=key
print(f"maximum value {max_value} with key:{max_key}")
               