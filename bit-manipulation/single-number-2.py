class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            s = 0
            for x in nums:
                s += abs(x)>>i & 1
            
            if s%3:
                ans+=2**i
        s = 0
        for x in nums:
            s += x>>i & 1
        if s%3:
            ans = (0-ans)

        return ans
