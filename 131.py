#Write a function to calculate grade based on marks.
def func_grade(marks):
    if marks>=90:
        print(f"your grade is A with marks {marks}.")
    elif marks>=75 and marks<=89:
        print(f"your grade is B with marks {marks}.")
    elif marks>=50 and marks<=74:
        print(f"your grade is C with marks {marks}.") 
    elif marks<50:
        print(f"oops!!! you are fail with marks {marks}.")
    return
func_grade(98)
func_grade(76)
func_grade(45)

