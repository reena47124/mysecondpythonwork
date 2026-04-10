#list
#remove duplicates from a list.
#method 2)
a=list(map(int,input("enter the elements:").split()))
b=[]
for num in a:
    if num not in b:
        b.append(num)
print(b)
        

