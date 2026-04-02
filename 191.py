#Write a function using **kwargs to print all key-value pairs.
def func_key(**kwargs):
    for key,value in kwargs.items():        #i.e. both for key and value
        print(f"{key}:{value}")
    return
func_key(name="radha",age=23,marks=99,city="pune")    
