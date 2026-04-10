#list
#merge two lists.
li1=list(map(int,input("enter elements of list 1:").split()))
li2=list(map(int,input("enter elements of list 2:").split()))
for num in li2:
    li1.append(num)
print(f"merged list:{li1}")

