#list
#find frequency of each element.
a=list(map(int,input("enter elements:").split()))
freq={}
n=len(a)
for i in range(n):
    if a[i] in freq:
        freq[a[i]]+=1
    else:
        freq[a[i]]=1
print(freq)
            