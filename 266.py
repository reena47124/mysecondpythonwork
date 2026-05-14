#list
#find the 2nd largest element in the list. without handling duplicates.
#method 1)
a=list(map(int,input("enter elements:").split()))
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
a.remove(maximum)   #modification of original list.
maximum=a[0]
for i in a:
    if i>maximum:
        maximum=i
print(f"2nd largest is:{maximum}")
