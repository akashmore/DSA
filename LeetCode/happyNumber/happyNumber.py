class Solution:
    def isHappy(self, n: int) -> bool:
        tmpSet = set()
        if n == 1:
            return True
        number = str(n)
        while number not in tmpSet:
            tmpSet.add(number) 
            summetion = 0
            for n in number:
                summetion = summetion + int(n)**2              
            number = str(summetion)            
            if number == "1":
                return True
        return False
            