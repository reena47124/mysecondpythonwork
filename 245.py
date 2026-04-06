#string.
#remove all spaces from a string.
s=input("enter a string:")
s1=""
target=" "
for ch in s:
    if ch!=target:
        s1=s1+ch
print(s1)
