class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        max_num = abs(nums[0] - nums[1])
        for i in range(len(nums)-1):
            max_num = max(max_num, abs(nums[i]-nums[i+1]))
        return max_num