#tuple
#count frequency of each element.
t=tuple(map(int,input("enter elements:").split()))
n=len(t)
freq={}
for i in range(n):
    if t[i] in freq:
        freq[t[i]]+=1
    else:
        freq[t[i]]=1
print(freq)
