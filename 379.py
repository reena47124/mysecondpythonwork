#set
#check if one set is a subset of another.
#method 1)
s1={1,2,3,4,5,6,7}
s2={1,2,3,4,5}
n2=len(s2)
s3=set()
for item in s2:
    if item in s1:
        s3.add(item)
n3=len(s3)
if n2==n3:
    print(f"s2 is a subset of s1")
else:
    print(f"s2 is not a subset of s1")  
