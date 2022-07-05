# we need to maintain max and min both and handle 0 case
class solution:
    def solve(self,nums):
        res = max(nums)
        curMin, curMax = 1,1
        for n in nums:
           tmp = curMax * n
           curMax = max(n*curMax,n*curMin,n)
           curMin = min(tmp,n*curMin,n)
           res = max(res,curMax)
        return res                       
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([2,3,-2,4])
    print(result)