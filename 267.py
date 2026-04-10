#list
#find the 2nd largest element in the list.
#method 2)
a=list(map(int,input("enter the elements:").split()))
a=list(set(a))   #removes all duplicates
a.sort()
print(f"2nd largest:{a[-2]}")

