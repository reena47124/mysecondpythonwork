#Write a normal function that takes a lambda as input and applies it on two numbers.
def func_one(a,b, op=lambda a,b:a+b):
    sum=op(a,b)
    square=sum*sum
    print(square)
    return
func_one(5,2)