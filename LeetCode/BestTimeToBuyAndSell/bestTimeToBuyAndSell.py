class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if prices[i] - minimum > diff:
                diff = max(diff,prices[i] - minimum)
            if prices[i] < minimum:
                minimum = prices[i]    
        return diff