#set
#find the intersection of two sets.
#method 3)
s1={1,2,3,4,5,'a',8}
s2={'a',3,'b',5,8}
s3=set()
for item in s1:
    if item in s2:
        s3.add(item)
print(f"intersection:{s3}")
        