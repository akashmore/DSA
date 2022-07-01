k = 5
n = 10
arr = [2,6,3,4,7,2,10,3,2,1]
avg = sum(arr) // len(arr)
for i in range(0,len(arr)):
    if arr[i] < avg:
        if arr[i] + k <= avg:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] - k
    else:
        if arr[i] - k >= avg:
            arr[i] = arr[i] - k
        else:
            arr[i] = arr[i] + k
print(max(arr) - min(arr))