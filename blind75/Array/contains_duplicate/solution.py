class solution:
    def solve(self,arr):
        tmp = {}
        for ele in arr:
            if ele not in tmp:
                tmp[ele]= 1
            else:
                return True
        return False
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([1,2,3,3])
    print(result)