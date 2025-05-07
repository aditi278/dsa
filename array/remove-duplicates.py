class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        i = 1
        num = nums[0]
        while i < n:
            if nums[i] == num:
                i+=1
                continue
            nums[k] = nums[i]
            num = nums[i]
            i+=1
            k+=1
        return k