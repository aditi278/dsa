class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        count = 0
        for x in nums:
            if x not in m:
                left = m.get(x-1, 0)
                right = m.get(x+1, 0)
                m[x] = left + right + 1
                m[x - left] = m[x]
                m[x + right] = m[x]
                count = max(count, m[x])
        return count
