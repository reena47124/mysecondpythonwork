#dictionary
#group the words that are anagrams.
words=['listen','silent','eat','tea','evil','study','eat','dusty','vile']
d={}
for word in words:
    key=''.join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word) 
print(d)
           