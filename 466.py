#file_handling in python
#count total characters in a file.
#method 1)
with open("demo.txt","r") as file:
    data=file.read()
    print(len(data))
