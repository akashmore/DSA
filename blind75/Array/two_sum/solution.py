from sympy import true


class solution:
   def solve(self,arr,target):
       tmp = {}
       for i in range(0,len(arr)):
           if arr[i] not in tmp:
               tmp[target-arr[i]] = i
           else:
               return (i,tmp[arr[i]])
            

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([3,3],6)
    print(result)
