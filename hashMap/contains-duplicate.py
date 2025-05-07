class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m.keys():
                m[nums[i]]=i
            elif i-m[nums[i]]<=k:
                return True
            else:
                m[nums[i]]=i
        return False
        