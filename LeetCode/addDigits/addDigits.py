class Solution:
    def addDigits(self, num: int) -> int:
        summetion = 0
        while num > 0:
            remainder = num % 10
            summetion = summetion + remainder
            num = num // 10
            if num == 0 and len(str(summetion))>1:
                num = summetion
                summetion = 0
        return summetion
                