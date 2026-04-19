#tuple
#reverse a tuple.
#method 3)
t=tuple(map(int,input("enter elements:").split()))
rev=()
n=len(t)
for i in range(n-1,-1,-1):
    rev=rev+(t[i],)
print(rev)
