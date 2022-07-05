import math
class solution:
    # def solve(self,arr):
    #     final_multiplication = 1
    #     for ele in arr:
    #         final_multiplication = final_multiplication * ele
    #     for i in range(0,len(arr)):
    #         arr[i] = final_multiplication // arr[i]
    #     return arr
    
    def solve(self,arr):
        res = [1 for i in range(len(arr))]
        prefix = 1
        for i in range(0,len(arr)):
            res[i] = prefix
            prefix*= arr[i]
        postfix = 1
        for j in range(len(arr)-1,-1,-1):
            res[j]*= postfix
            postfix*=arr[j]
        return res
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([1,2,3,4])
    print(result)
    