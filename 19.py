#take marks and print grade(A,B,C,fail).
marks=float(input("enter marks of the student:"))
if marks>90 and marks<=100:
    print("wow!!! congratulations your grade is A")
elif marks>70 and marks<=90:
    print("your grade is B")
elif marks>50 and marks<=70:
    print("your grade is C")
else:
    print("oopsss!!!! sorry, you are fail.")            