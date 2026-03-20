#use logical operators to check age eligibility i.e. 18+.
age=int(input("enter your age:"))
if age>=1 and age<18:
    print("oops!!! not eligible, sorry.")
elif age>=18:
    print("congratulations you are eligible!")

