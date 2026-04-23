#set
#find the union of two sets.
#method 3)
s1={1,2,3,4,5,'a',8}
s2={'a',3,'b',5,8}
for item in s1:
    s2.add(item)
print(f"union:{s2}")
