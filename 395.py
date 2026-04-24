#sets
#find the first repeating element in a list using a set.
li=list(map(int,input("enter the elements of the list:").split()))
seen=set()
for item in li:
    if item in seen:
        print(item)
        break
    else:
        seen.add(item)
        
