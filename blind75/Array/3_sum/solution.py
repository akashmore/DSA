class solution:
    #returning tuples
    # def solve(self,arr):
    #     arr.sort()
    #     ele_set = set()
    #     for i in range(0,len(arr)):
    #         first = arr[i]
    #         start,end  = i+1, len(arr)-1
    #         while start < end:
    #             if arr[start] + arr[end] + arr[first] == 0:
    #                 ele_set.add((arr[first],arr[start],arr[end]))
    #                 start+=1
    #             elif arr[start] + arr[end] + arr[first] < 0:
    #                 start+=1
    #             else:
    #                 end-=1
    #     return ele_set
    
    #returning array
    def solve(self,arr):
        arr.sort()
        res = []
        for index,value in enumerate(arr):
            if(index > 0 and value== arr[index-1]):
                continue
            l,r = index + 1, len(arr) - 1
            while(l<r):            
                su = value + arr[l] + arr[r]
                if(su>0):
                    r-=1
                elif(su<0):
                    l+=1
                else:
                    res.append([value,arr[l],arr[r]])
                    l+=1
                    while arr[l] == arr[l-1] and  l < r:
                        l+=1
        return res
        
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([-1,0,1,2,-1,-4])
    print(result)