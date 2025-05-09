class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        csum=0
        min_len = n+1
        r=0
        l=0
        while l < n:
            while r < n and csum < target:
                csum+=nums[r]
                r+=1
            if csum >= target:
                min_len = min(min_len, r-l)
            csum-=nums[l]
            l+=1
            while l<n and csum >= target:
                min_len = min(min_len, r-l)
                csum-=nums[l]
                l+=1    
        if min_len <= n:
            return min_len
        return 0