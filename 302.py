#tuple
#find the length of the tuple without using len().
t=tuple(map(int,input("enter elements:").split()))
length=0
for items in t:
    length+=1
print(length)
    