#tuple
#find the index of an element.
t=tuple(map(int,input("enter elements:").split()))
ele=int(input("enter the element:"))
count=0
for item in t:
    if item==ele:
        print(count)
        break
    else:
        count+=1
