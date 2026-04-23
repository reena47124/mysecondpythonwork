#set
#check if one set is a subset of another.
#method 2)
s1={1,2,3,4,5,6,7}
s2={1,2,3,4,5}
is_subset=True
for item in s2:
    if item not in s1:
        is_subset=False
        break
if is_subset:
    print(f"s2 is subset of s1")
else:
    print(f"s2 is not a subset of s1")
            
