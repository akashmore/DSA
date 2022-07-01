
#Approach 1 using extra space
# import copy
# arr = [1,2,3,4,5]
# k = 3
# tmp = copy.deepcopy(arr)
# for i in range(0,len(arr)):
#     if i+k >= len(arr):
#         index = (i+k) % len(arr)
#         tmp[index] = arr[i]
#     else:
#         tmp[i+k] = arr[i]
# for j in range(0,len(arr)):
#     arr[j] = tmp[j]
# print(arr) 

#approach 2 by reversing k elements of array
arr = [1,2,3,4,5]
k = 3
second_half_array = arr[len(arr)-k:]
first_half_array = arr[:len(arr)-k]
arr = second_half_array[::-1]+first_half_array
print(arr)
