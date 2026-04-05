#re-arrange an array in alternating positive and negative numbers.
import array
nums=list(map(int,input("enter the elements:").split()))
arr=array.array('i',nums)
pos=array.array('i')
neg=array.array('i')
for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
result=array.array('i')
i=j=0
while i<len(pos) and j<len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i+=1
    j+=1
result.extend(pos[i:])
result.extend(neg[j:])
print(result)
    


