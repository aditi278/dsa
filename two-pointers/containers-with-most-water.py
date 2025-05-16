class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) - 1
        l = 0
        vol = (r-l)*min(height[l], height[r])
        while r > l:
            if height[r]>height[l]:
                l+=1
            else:
                r-=1

            vol = max(vol, (r-l)*min(height[l], height[r]))
        return vol
        