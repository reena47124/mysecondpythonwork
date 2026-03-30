#Write a function to count digits in a number.
def func_count(num):
    count=0
    while num!=0:
        digit=num%10
        count+=1
        num=num//10
    print(f"there are total {count} digits in a given number.")
    return count
func_count(1)
func_count(1232)
    