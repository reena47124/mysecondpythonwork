#Write a function that takes **kwargs and prints only values greater than 50.
def func_grt(**kwargs):
    for key,value in kwargs.items():
        if value>50:
            print(f"{key}:{value}")
    return
func_grt(a=12,b=78,c=56,d=90,e=3)        