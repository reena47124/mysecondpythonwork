#tuple
#swap two tuples.
t1=tuple(map(int,input("enter elements of 1st tuple:").split()))
t2=tuple(map(int,input("enter elements of 2nd tuple:").split()))
t1,t2=t2,t1
print(f"t1:{t1}")
print(f"t2:{t2}")
