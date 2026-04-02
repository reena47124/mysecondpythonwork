#Write a function that shows the difference between:
#positional argument
#keyword argument
def func_dif(a,b,c,name,age,city):
    print(f"{a},{b},{c} are positional arguments.")
    print(f"name:{name},age:{age},city:{city} are keyword arguments.")
    return
func_dif(12,56,34,name="radha",age=24,city="pune")
