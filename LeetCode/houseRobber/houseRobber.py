class Solution:
    def rob(self, nums: List[int]) -> int:
        rob0,rob1 = 0,0
        for n in nums:
            tmp = max(n+rob0,rob1)
            rob0=rob1
            rob1 = tmp
        return rob1