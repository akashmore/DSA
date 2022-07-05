class solution:
   def solve(self,arr):
        minimum_buy = arr[0]
        max_profit = 0
        for ele in arr:
            minimum_buy = min(minimum_buy,ele)
            max_profit = max(max_profit,ele-minimum_buy)
        return max_profit
            
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([7,6,4,3,1])
    print(result)
