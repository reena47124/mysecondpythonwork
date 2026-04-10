#list
#find the 2nd largest element in the list.
#method 4)
a=list(map(int,input("enter the elements:").split()))
first=second=float('-inf')
for num in a:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(f"second largest:{second}")
            