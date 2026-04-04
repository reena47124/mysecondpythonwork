#Write a program to take N inputs from user and store them in an array.
import array
def func_inputs(n):
    arr=array.array('i')
    for i in range(n):
        num=int(input(f"enter the {i+1}th value:"))
        arr.append(num)
    print(f"array:{arr}")
    return arr
n=int(input(f"enter the value of n:"))
func_inputs(n)

    