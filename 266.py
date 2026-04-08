#list
#find the 2nd largest element in the list. without handling duplicates.
a=list(map(int,input("enter elements:").split()))
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
a.remove(maximum)
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
print(f"2nd largest is:{maximum}")
