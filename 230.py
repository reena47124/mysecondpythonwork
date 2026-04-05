#find the frequency of each element.
import array
nums=list(map(int,input("enter the elements of array:").split()))
arr=array.array('i',nums)
freq={}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
print(freq) 
