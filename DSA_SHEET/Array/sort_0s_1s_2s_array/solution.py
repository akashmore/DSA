arr = [0,2,1,2,0]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)
        