class solution:
    def solve(self,arr):
        max_sum = arr[0]
        summetion = 0
        for ele in arr:
            if summetion < 0:
                summetion = 0
            summetion += ele
            max_sum = max(summetion,max_sum)
        return max_sum            
        
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([5,4,-1,7,8])
    print(result)