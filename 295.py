#list
#find the first non-repeating element.
a=list(map(int,input("enter elements:").split()))
for num in a:
    a.count(num)
    if a.count(num)==1:
        print(num)
        break
    