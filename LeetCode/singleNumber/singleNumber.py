class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmpDict = {}
        for n in nums:
            if n not in tmpDict:
                tmpDict[n]=1
            else:
                tmpDict[n]+=1
        for re_ele in tmpDict:
            if tmpDict[re_ele] ==1:
                return re_ele