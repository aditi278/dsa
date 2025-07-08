class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        n = len(nums)
        for i in range(n-1):
            left = i+1
            right = n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == target:
                    return curr
                if abs(target - curr) < abs(target - closest):
                    closest = curr
                if curr > target:
                    right -= 1
                else:
                    left += 1
        
        return closest