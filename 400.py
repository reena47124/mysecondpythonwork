#sets
#count distinct elements in a list.
li=list(map(int,input("enter the elements of the list:").split()))
s=set(li)
count=0
for item in s:
    count+=1
print(count)
    