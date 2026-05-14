#file_handling in python
#delete a student record
import csv
rows=[]
name="karan"
with open("student.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        if row[0]!=name:
            rows.append(row)
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(rows) 
print(f"{name} record deleted successfully")
               
