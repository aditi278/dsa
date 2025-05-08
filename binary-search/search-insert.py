class Solution:
    def search(self, nums, target, start, end, n, level=0):
        if end < start:
            return -1
        
        mid = start + (end - start + 1)//2

        if mid+1 < n and nums[mid] < target and nums[mid+1] > target:
            return mid+1
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            val = self.search(nums, target, start, mid-1, n, level+1)
            if val is not None and val != -1:
                return val
        elif target > nums[mid]:
            val = self.search(nums, target, mid+1, end, n, level+1)
            if val is not None and val != -1:
                return val
        else:
            return mid+1
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        if target < nums[0]:
            return 0
        if target > nums[end]:
            return n
        return self.search(nums, target, start, end, n)
