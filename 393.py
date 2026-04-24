#set
#find common elements between two lists using sets.
l1=list(map(int,input("enter the elements of the first list:").split()))
l2=list(map(int,input("enter the elements of the second list:").split()))
result=(set(l1)&set(l2))
print(result)
