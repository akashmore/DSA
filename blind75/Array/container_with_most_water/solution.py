class solution:
    def solve(self,arr):
        max_vol = arr[0]
        i,j = 0,len(arr)-1
        while i < j:
            volume = min(arr[i],arr[j]) * (j-i)
            max_vol = max(max_vol,volume)
            if arr[i] < arr[j]:
                i+=1
            else:
                j-=1
        return max_vol
            
       
           
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([1,1])
    print(result)