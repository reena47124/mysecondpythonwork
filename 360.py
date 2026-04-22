#dictionary
#count frequency of characters in a string.
s=input("enter the string:")
freq={}
for ele in s:
    if ele in freq:
        freq[ele]+=1
    else:
        freq[ele]=1
print(freq)
            