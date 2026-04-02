#Write a function that accepts positional + keyword arguments together.
def func_both(a,b,c,d,e):
    sum=a+b+c+d+e
    print(sum)
    return sum
func_both(12,45,2,d=11,e=3)
