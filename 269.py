#list
#find the 2nd largest element in the list.
#method 3)
a=list(map(int,input("enter the elements:").split()))
a=list(set(a))
maximum=a[0]
for num in a:
    if num>maximum:
        maximum=num
a.remove(maximum)
maximum=a[0]
for num in a:
    if num>maximum:
        maximum=num
print(f"second largets:{maximum}")
                