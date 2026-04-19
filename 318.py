#tuple
#find the index of an element.
#method 2)
t=tuple(map(int,input("enter elements:").split()))
ele=int(input("enter the element:"))
count=0
found=False
for item in t:
    if item==ele:
        print(f"index:{count}")
        found=True
        break
    else:
        count+=1
if not found:
    print(f"element is not found.")
            