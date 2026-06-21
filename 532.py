#rotate a list by one position
li=[1,2,3,4,5,6,7]
print(f"list before rotation:",li)
li=[li[-1]]+li[:-1]
print(f"list after rotation",li)