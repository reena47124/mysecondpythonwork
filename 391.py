#set
#check if two sets are disjoint.
s1={1,2,3,4,5,6,7}
s2={1,2,3,4,5}
is_disjoint=True
for item in s1:
    if item in s2:
        is_disjoint=False
        break
if is_disjoint:
    print("sets are disjoint.")
else:
    print("sets are not disjoint")
            