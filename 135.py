#Write a function to print even numbers from 1 to N.
def func_even(n):
    print(f"all even numbers are:")
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=",")
    print()   
    return
func_even(23)
func_even(13)
