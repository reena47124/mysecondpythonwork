#count numbers with exactly 3 divisors.
#method 1)
num=int(input("enter the number:"))
sum=0
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==3:
        print(i)
        sum+=1
print(f"there are {sum} numbers which have exactly 3 divisors.")        
