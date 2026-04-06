#string.
#check whether a character exists in a string.
s=input("enter a string:")
target='a'
for ch in s:
    if ch==target:
        print(f"exists!")
        break
else:
    print(f"doesnt exist!")
