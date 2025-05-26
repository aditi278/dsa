class Solution:
    def findMin(self, nums: List[int], start=0, end=None) -> int:
        if end is None:
            end = len(nums) - 1
        
        if nums[start] < nums[end]:
            return nums[start]
        if end == start:
            return nums[start]
        if end < start:
            return
        mid = (start+end)//2
        if nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[start] <= nums[mid]:
            return self.findMin(nums, mid+1, end)
        else:
            return self.findMin(nums, start, mid)