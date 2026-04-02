#Write a function using *args to find the maximum number.
def func_maxi(*args):
    maxi=0
    for num in args:
        if num>maxi:
            maxi=num
    print(maxi)
    return maxi
func_maxi(12,89,23,90,11)        
