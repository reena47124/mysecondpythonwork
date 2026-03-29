#find all unique prime factors of a given number.
num=int(input("enter the number:"))
temp=num
a=[]
i=2
while i<num:
    if num%i==0:
        a.append(i)
        while num%i==0:
            num=num//i
    i+=1
if num>1:
    a.append(num)    
print(f"all prime factors of a given number {temp} are {a}")               