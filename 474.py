#file_handling in python
#search student by name
import csv
with open("student.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    name="radha"
    for row in reader:
        if name==row[0]:
            print(f"{name} exists")
            break
    else:
        print(f"name doesnt exist")


             
