#find the first non-repeating element.
import array
nums=list(map(int,input("enter the elements:").split()))
a=array.array('i',nums)
for i in a:
    a.count(i)
    if a.count(i)==1:
        print(i)
        break
        