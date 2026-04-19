#tuple
#create a tuple of square from 1 to n.
n=int(input("enter the value of n:"))
t=tuple(map(int,input("enter elements:").split()))
li=list(t)
li1=[]
for num in li:
    li1.append(num*num)
t1=tuple(li1)
print(t1)
