#Write a function to reverse a string.
def func_rev(s):
    rev=s[::-1]
    print(f"reverse of string {s} is {rev}")
    return rev
func_rev("hellothere!")