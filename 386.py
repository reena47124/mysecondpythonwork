#set
#find the symmetric difference between two sets.
#method 3)
s1={1,2,3,4,5,'a',8}
s2={'a',3,'b',5,8}
s3=set()
for item in s1:
    if item not in s2:
        s3.add(item)
for item in s2:
    if item not in s1:
        s3.add(item)
print(s3)
                