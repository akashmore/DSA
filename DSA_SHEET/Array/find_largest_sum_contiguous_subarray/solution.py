#Also known as kadane's algorithm

arr = [1,2,3,-2,5]
max_sum = arr[0]
_sum = 0
for ele in arr:
    _sum +=ele
    max_sum = max(max_sum,_sum)
    if _sum < 0:
        _sum = 0
print(max_sum)