class Solution:
    def findPeakElement(self, nums: List[int], start=0, end=None) -> int:
        n = len(nums)
        if end is None:
            end = n - 1
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        if start == end:
            return start
        
        
        mid = start + (end-start)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[mid-1]:
            return self.findPeakElement(nums, mid, end)
        else:
            return self.findPeakElement(nums, start, mid)