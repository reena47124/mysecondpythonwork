#Write a function where default argument comes after non-default argument (understand rule).
def func_default(a,b,c=90,d=23):
    sum=a+b+c+d
    print(sum)
    return sum
func_default(25,77)

