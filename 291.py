#list
#move all zeros to the end of the list.
a=list(map(int,input("enter elements:").split()))
b=[]
c=[]
for num in a:
    if num==0:
        b.append(num)
    else:
        c.append(num) 
for num in b:
    c.append(num)
print(c)
               