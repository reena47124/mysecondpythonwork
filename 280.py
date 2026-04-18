#list
#separate even and odd numbers.
a=list(map(int,input("enter elements:").split()))
even_list=[]
odd_list=[]
for num in a:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(f"even:{even_list}")
print(f"odd:{odd_list}")

           