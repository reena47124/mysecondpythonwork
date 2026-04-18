#list
#rearrange list in alternative positive and negative numbers.
a=list(map(int,input("enter elements:").split()))
pos=[]
neg=[]
for num in a:
    if num<0:
        neg.append(num)
    else:
        pos.append(num)
result=[]
i=j=0
while i<len(pos) and j<len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i+=1
    j+=1
result.extend(pos[i:])
result.extend(neg[j:])
print(result)
                  