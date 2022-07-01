class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmpSet = set()
        for ele in nums:
            if ele in tmpSet:
                return True
            else:
                tmpSet.add(ele)
        return False