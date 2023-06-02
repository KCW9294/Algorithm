N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

result = []
for i in arr2:
    if count_by_range(arr1, i, i)>0:
        result.append(1)
    else:
        result.append(0)

for j in result:
    print(j)