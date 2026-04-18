#list
#find duplicate elements in a list.
a=list(map(int,input("enter elements:").split()))
b=[]
d=[]
for num in a:
    if num in b and num not in d:
        d.append(num)
    else:
        b.append(num)
print(f"duplicates:{d}")
print(f"list after removing duplicates:{b}")
            




