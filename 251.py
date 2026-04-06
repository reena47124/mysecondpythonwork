#string.
#sort characters in a string alphabetically.
#method 2: without using sorted() method.
s=input("enter a string:")
s=list(s)
n=len(s)
for i in range(n):
    for j in range(i+1,n):
        if s[i]>s[j]:
            s[i],s[j]=s[j],s[i]
s1="".join(s) 
print(s1)
           