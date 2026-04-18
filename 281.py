#list
#find all prime numbers in a list.
a=list(map(int,input("enter elements:").split()))
for num in a:
    if num>1:
        is_prime=True
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                is_prime=False
                break
        if is_prime:
            print(num,end=",")



