#tuple
#check if an element exists in a tuple.
t=tuple(map(int,input("enter elements:").split()))
target=int(input("enter element:"))
for item in t:
    if item==target:
        print("exists!")
        break
