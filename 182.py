#Write a function that accepts keyword arguments and prints them.
def fun_key(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    return
fun_key(name="Radha",age=24,marks=99,grade="A")    