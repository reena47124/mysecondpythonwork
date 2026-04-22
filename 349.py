#dictionary
#find the key with minimum value.
d={1:23,2:34,3:12,4:78,5:35}
min_key=None
min_value=float('inf')
for key,value in d.items():
    if value<min_value:
        min_value=value
        min_key=key
print(f"minimum value {min_value} with key:{min_key}")
        