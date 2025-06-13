class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left+right)//2
            pairs = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= mid:
                    pairs+=1
                    i+=1
                i+=1
            if pairs >= p:
                right = mid
            else:
                left = mid+1

        return left