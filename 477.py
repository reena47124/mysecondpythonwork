#file_handling in python
#sort students by marks.
import csv
data=[]
with open("student.csv","r") as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        data.append(row)
    n=len(data)
    for i in range(n):
        for j in range(i+1,n):
            if int(data[i][2])>int(data[j][2]):
                data[i],data[j]=data[j],data[i]

#with open("student.csv","w",newline="") as file:
    #writer=csv.writer(file)
    #writer.writerow(header)
    #writer.writerows(data)
#print(f"sorted successfully")

print(header)
for row in data:
    print(row)
    

    





