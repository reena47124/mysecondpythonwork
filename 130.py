#Write a function to check if a year is a leap year.
def func_leap(year):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    return
func_leap(2000)
func_leap(1900)
func_leap(1800)
func_leap(2020)        