class solution:
    def solve(self,arr):
        res = arr[0]
        left,right = 0, len(arr)-1
        while left < right:
            if arr[left] < arr[right]:
                res = min(res,arr[left])
                break
            middle = (left + right) // 2
            res = min(res,arr[middle])
            if arr[middle] >= arr[right]:
                left = middle + 1
            else:
                right = middle - 1
        return res
                       
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([3,4,5,1,2])
    print(result)