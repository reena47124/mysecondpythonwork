#file_handling in python
#count total student.
import csv
with open("student.csv","r") as file:
    reader=csv.reader(file)
    next(reader)   #skip header row
    count=0
    for row in reader:
        count+=1
print(f"total students are:{count}")
        