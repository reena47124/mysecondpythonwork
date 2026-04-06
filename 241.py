#string.
#reverse a string without using slicing().
s=input("enter a string:")
s1=""
n=len(s)
for i in range(n-1,-1,-1):
    s1=s1+s[i]
print(s1)

