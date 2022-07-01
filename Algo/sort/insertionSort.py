#comapare every element with its all previos array and place appropriate
arr = [1,10,2,3,8,4,7,9,5,6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
    arr[j+1] = key
print(arr)