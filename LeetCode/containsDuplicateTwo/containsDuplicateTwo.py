class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp = {}
        for i in range(0,len(nums)):
            if nums[i] not in tmp:
                tmp[nums[i]] = i
            else:
                if abs(tmp[nums[i]] - i) <= k:
                    return True
                else:
                    tmp[nums[i]] = i               
        return False
        