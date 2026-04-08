#string.
#toggle case of each character.
#method 2: without using swapcase() method
s=input("enter a string:")
s1=""
for ch in s:
    if ch.islower():
        s1=s1+ch.upper()
    elif ch.isupper():
        s1=s1+ch.lower()
    else:
        s1=s1+ch
print(s1)
                