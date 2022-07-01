class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(0,n-1):
            tmp = a
            a = a + b
            b = tmp
        return a