#file_handling in python
#attendance system, store:name,date,present/absent.
import csv
while True:
    print(f"1) add attendance")
    print(f"2) veiw attendance")
    print(f"3) search a particular student's attendance")
    print(f"4) exit!")
    choice=input("enter the choice:")

    if choice=="1":
        name=input("enter the name of the student:")
        date=input("enter the date (dd/mm/yy):")
        status=input("enter present/absent:")
        with open("attendance.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([name,date,status])
        print(f"attendance added successfully")

    elif choice=="2":
        with open("attendance.csv","r") as file:
            reader=csv.reader(file) 
            print("attendance record:")
            for row in reader:
                print(row)

    elif choice=="3":
        search_name=input("enter the name of the student you want to search:")
        found=False
        with open("attendance.csv","r") as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0].lower()==search_name.lower():
                    print(row)
                    found=True
        if found==False:
            print(f"{search_name} not found")

    elif choice=="4":
        print(f"you exited successfully!")
        break

    else:
        print(f"invalid input!")





                           