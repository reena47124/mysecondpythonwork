#file_handling in python
#find average marks
import csv
with open("student.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    sum=0
    count=0
    for row in reader:
        sum=sum+int(row[2])
        count+=1
avg_marks=sum/count
print(f"average marks:{avg_marks}")
