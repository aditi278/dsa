class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_diff = nums[1] - nums[0]
        for i in range(1, len(nums)):
            if nums[i] - min_num > 0:
                max_diff = max(max_diff, nums[i] - min_num)
            if nums[i] < min_num:
                min_num = nums[i]
        return max_diff if max_diff > 0 else -1