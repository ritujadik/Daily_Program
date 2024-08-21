from functools import reduce
def add(acc,num):
    return acc + num
def findmissingno(arr):
    min_no = min(arr)
    max_no = max(arr)
    total_sum = ((max_no + min_no-1)*(max_no + min_no))/2
    arr_sum = reduce(add,arr,0)
    missing_no = total_sum - arr_sum
    return missing_no


result = findmissingno([1,2,3,4,5,6,7,9]);
print(result)