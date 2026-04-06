#string.
#count frequency of each character.
s=input("enter a string:")
n=len(s)
for i in range(n):
    if s[i] not in s[:i]:
        print(f"{s[i]}:{s.count(s[i])}")
    
