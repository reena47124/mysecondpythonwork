#file_handling in python
#append new student data.
import csv
with open("student.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["kunti",30,92])
    