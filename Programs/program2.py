import copy
def cntIndexesToMakeBalance(arr, n):
    for i in range(0,n):
        new_array = copy.deepcopy(arr)
        new_array.remove(arr[i])
        check = calculate_sum(new_array,len(new_array))
        if check:
            return i+1
    return -1
        
        
    

def calculate_sum(array,n):
    even_sum = 0
    odd_sum = 0
    for i in range(0,n):
        if i%2 == 0:
            even_sum += array[i]
        else:
            odd_sum += array[i]
    return even_sum == odd_sum 
   
# Driver Code
if __name__ == "__main__" :
 
    arr = [2,5,6,7,8,4]
    n = len(arr)
     
    print(cntIndexesToMakeBalance(arr, n))