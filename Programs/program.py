# from collections import defaultdict
# import math
class Solution:   
    def do(self, s):
        tmp = {}
        for ele in s:
            if ele in tmp:
                tmp[ele] = tmp[ele] + 1
            else:
                tmp[ele] = 1
        sum = 0
        present_odd = False
        for key,value in tmp.items():
            if value % 2 == 0:
                sum=sum+value
            else:
                present_odd = True
                sum = sum+ (value - 1)
        return sum + 1 if present_odd else sum 
        
                            
                           
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.do("bb"))
