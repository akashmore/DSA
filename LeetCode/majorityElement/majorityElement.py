class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        degree = len(nums)//2
        tmpDict = {}
        for ele in nums:
            if ele not in tmpDict:
                tmpDict[ele]=1
            else:
                tmpDict[ele]+= 1
        for ele1 in tmpDict:
            if tmpDict[ele1] > degree:
                return ele1