#list
#find the length of the list without using len().
a=list(input("enter the elements:").split())
count=0
for i in a:
    count+=1
print(f"length of the list is:{count}") 
