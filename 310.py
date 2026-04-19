#tuple
#find the maximum and minimum element.
t=tuple(map(int,input("enter elements:").split()))
maximum=minimum=0
for item in t:
    if item>maximum:
        maximum=item
    elif item<minimum:
        minimum=item
print("maximum:",maximum)
print("minimum:",minimum) 
               