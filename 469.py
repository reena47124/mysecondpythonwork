#file_handling in python
#store 5 students data in csv file with columns:name,age,marks.
import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","marks"])
    writer.writerow(["radha",21,99])
    writer.writerow(["kanha",24,98])
    writer.writerow(["karan",23,90])
    writer.writerow(["arjun",22,96])
    writer.writerow(["bheem",25,89])
    