#set
#find all duplicates in a list using a set.
li=list(map(int,input("enter elements of a list:").split()))
seen=set()
dup=set()
for item in li:
    if item in seen:
        dup.add(item)
    else:
        seen.add(item)
print(f"duplicates:{dup}")
print(f"seen:{seen}")
