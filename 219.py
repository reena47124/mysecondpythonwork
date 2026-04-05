#find the duplicate elemetns in an array.
import array
nums=list(map(int,input("enter the elements of the array:").split()))
a=array.array('i',nums)
n=len(a)
b=array.array('i')
for i in range(n):
    for j in range(i+1,n):
        if a[i]==a[j] and a[i] not in b:
            b.append(a[i])
            
print(f"duplicate elements are:{b}")



