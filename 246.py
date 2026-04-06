#string.
#replace all vowels with *.
s=input("enter a string:")
s1=""
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        s1=s1+"*"
    else:
        s1=s1+ch
print(s1)
            


