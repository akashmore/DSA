class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_set = sorted(set(nums),reverse=True)
        if len(sorted_set)<3:
            return max(sorted_set)
        else:
            return sorted_set[2]