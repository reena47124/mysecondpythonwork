#find missing number
def missing(arr):

    n = len(arr)+1

    total = n*(n+1)//2

    return total-sum(arr)
print(missing([1,2,4,5,6]))