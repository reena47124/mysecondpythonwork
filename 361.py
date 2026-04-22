#dictionary
#find the first non-repeating character using a dictionary.
s=input("enter the string:")
freq={}
for ele in s:
    if ele in freq:
        freq[ele]+=1
    else:
        freq[ele]=1
for ele in s:
    if freq[ele]==1:
        print(ele)
        break
                