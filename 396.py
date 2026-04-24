#sets
#check if a list contains duplicates.
li=list(map(int,input("enter the elements of the list:").split()))
seen=set()
is_contain=True
for item in li:
    if item in seen:
        is_contain=False
        break
if is_contain:
    print(f"yes")
else:
    print(f"no")
            
     

