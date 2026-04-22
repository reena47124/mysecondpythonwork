#sets
#check if an element exist in a set.
s={'s','1','4','f','9','j','k'}
ele=input("enter an element you want to check:")
for item in s:
    if ele==item:
        print("exist!")
        break
else:
    print("element doesnt exist.")
