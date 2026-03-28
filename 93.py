#decimal to binary conversion program.
n=int(input("enter the value of n:"))
n1=n   #store the original value of n
a=[]
while n!=0:
    b=n%2
    a.append(b)
    n=n//2
bin=a[::-1]  
bin_str=''.join(map(str,bin))   #to convert and join into single string
print(f"the binary conversion of the given number {n1} is {bin_str}")