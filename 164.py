#write a function to count number of zeros in a number.
def func_check(num):
    if num<0:  #handling negative number case
        num=abs(num)
    if num==0:    #handling edge case
        return 1
    count=0
    while num!=0:
        digit=num%10
        if digit==0:
            count+=1
        num=num//10
    return(count)
print(func_check(12098309800)) 
print(func_check(0)) 
print(func_check(-1092009000))      