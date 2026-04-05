#merge 2 arrays alternatively.
import array
num1=list(map(int,input("enter elements of first array:").split()))
num2=list(map(int,input("enter elements of second array:").split()))
arr1=array.array('i',num1)
arr2=array.array('i',num2)
arr3=array.array('i')
i=j=0
while i<len(arr1) and j<len(arr2):
    arr3.append(arr1[i])
    arr3.append(arr2[j])
    i+=1
    j+=1
arr3.extend(arr1[i:])
arr3.extend(arr2[j:])
print(f"final merged array:{arr3}")
    