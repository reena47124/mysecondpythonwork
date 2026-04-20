#dictionary
#check if a key exists in a dictionary.
d={1:"a",2:"b",3:"c"}
k=int(input("enter the value of k:"))
for key in d:
    if key==k:
        print("exists!")
        break
        
else:
    print("doesnt exist") 
