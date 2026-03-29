#find all factors of a positive number.
num=int(input("enter the number:"))
a=[]
sum=0
for i in range(1,num+1):
    if num%i==0:
        a.append(i)
        sum+=1
print(f"there are {sum} factors of the given number as {a}")