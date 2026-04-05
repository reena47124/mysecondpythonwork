#check if an array is a palindrome.
import array
nums=list(map(int,input("enter elements:")))
arr=array.array('i',nums)
n=len(arr)
rev=array.array('i')
for i in range(n-1,-1,-1):
    rev.append(arr[i])
print(rev)    