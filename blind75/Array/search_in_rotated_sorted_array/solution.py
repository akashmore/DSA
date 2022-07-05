class solution:
    def solve(self,nums,target):
        i,j = 0,len(nums)-1
        while i <= j:
            middle = (i+j)// 2
            if nums[middle] == target:
                return middle
            else:
                if nums[i] <= nums[middle]:
                    if nums[i] <= target < nums[middle]:
                        j = middle - 1
                    else:
                        i = middle + 1
                else:
                    if nums[middle] < target <= nums[j]:
                        i = middle + 1
                    else:
                        j = middle - 1 
        return -1        
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([4,5,6,7,0,1,2],0)
    print(result)