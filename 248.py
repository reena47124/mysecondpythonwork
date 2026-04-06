#string.
#remove duplicate characters.
s=input("enter a string:")
s1=""
for ch in s:
    if ch not in s1:
        s1=s1+ch
print(s1)
        