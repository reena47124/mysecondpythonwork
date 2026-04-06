#string.
#find the first non-repeating character.
s=input("enter a string:")
n=len(s)
for i in range(n):
    if s.count(s[i])==1:
        print(s[i])
        break
    