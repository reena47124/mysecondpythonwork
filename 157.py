#Write a recursive function to reverse a number.
def func_rev(num):
    if num==0:
        return 0
    print(num%10,end="")
    func_rev(num//10)
func_rev(23467)