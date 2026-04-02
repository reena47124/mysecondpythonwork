#Write a function that takes normal argument + *args and prints both separately.
def func_print(*args,a,b):
    print(f"normal arguments are:{a},{b}.")
    print(f"*args arguments are:")
    for num in args:
        print(f"{num}")
    return
func_print(2,4,78,45,a=12,b=11)