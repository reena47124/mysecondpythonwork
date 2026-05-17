#exceptional handling in python
#handle multiple exceptions in one program
try:
    a=int(input("enter the value of a:"))
    result=10/a
    print(f"result:{result}")
except ZeroDivisionError:
    print(f"cannot divide by zero")
except ValueError:
    print(f"invalid input") 
except Exception as e:
    print(f"some error occured!")
               
