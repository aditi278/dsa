class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [0]*n
        steps[0] = 0
        j = 1
        for i in range(n):
            jumps = nums[i]
            while j < n and j <= i + jumps:
                steps[j] = steps[i]+1
                j+=1
            if j == n:
                return steps[n-1]

        return steps[n-1]