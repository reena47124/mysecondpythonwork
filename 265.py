#list
#find the maximum and minimum element in the list.
a=list(map(int,input("enter elements:").split()))
maximum=a[0]
minimum=a[0]
for ele in a:
    if ele>maximum:
        maximum=ele
    if ele<minimum:
        minimum=ele
print(f"maximum:{maximum} and minimum:{minimum}")

