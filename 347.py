#dictionary
#count frequency of element   in a list using dictionary.
a=list(map(int,input("enter elements of the list:").split()))
freq={}
n=len(a)
for i in range(n):
    if a[i] in freq:
        freq[a[i]]+=1
    else:
        freq[a[i]]=1
print(freq)
            