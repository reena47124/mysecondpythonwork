#file_handling in python
#count total characters in a file.
#method 2)
file=open("name.txt","r")
data=file.read()
print(len(data))
file.close()
