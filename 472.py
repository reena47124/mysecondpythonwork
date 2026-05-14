#file_handling in python
#find highest marks
import csv
with open("student.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    highest_marks=0
    for row in reader:
        marks=int(row[2])
        if marks>highest_marks:
            highest_marks=marks 
print(f"highest marks:{highest_marks}") 
