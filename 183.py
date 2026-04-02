#Write a function that accepts keyword arguments and prints them.
def func_key(**kwargs):
    print(f"my name is {kwargs.get('name')}.i am {kwargs.get('age')} years old. i obtained {kwargs.get('marks')} marks. i live in {kwargs.get('city')}.")
    return
func_key(name="radha",age=24,marks=99,city="pune")

 