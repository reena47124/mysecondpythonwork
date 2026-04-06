#string.
#find the most frequent character.
s=input("enter a string:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
max_char=""
max_count=0
for key in freq:
    if freq[key]>max_count:
        max_count=freq[key]
        max_char=key
print(f"maximum times occuring character is:{max_char} with frequency:{max_count}")

                    