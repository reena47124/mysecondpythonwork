#set
#check if one set is a superset of another.
#method 2)
s1={1,2,3,4,5,6,7}
s2={1,2,3,4,5}
is_superset=True
for item in s2:
    if item not in s1:
        is_superset=False
        break
if is_superset:
    print(f"s1 is a superset of s2")
else:
    print(f"s1 is not a superset of s2") 
           