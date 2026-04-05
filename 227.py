#merge 2 arrays.
import array
num1=list(map(int,input("enter elements of first array:").split()))
num2=list(map(int,input("enter elements of second array:").split()))
arr1=array.array('i',num1)
arr2=array.array('i',num2)
for i in arr2:
    arr1.append(i)
print(f"merged array:{arr1}")    

