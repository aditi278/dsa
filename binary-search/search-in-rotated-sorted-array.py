class Solution:
    def search(self, nums: List[int], target: int, start=0, end=None) -> int:
        if end is None:
            end = len(nums) - 1
        if end < start:
            return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]: 
            if target >= nums[start] and target < nums[mid]:
                return self.search(nums, target, start, mid-1)
            else:
                return self.search(nums, target, mid+1, end)
        elif nums[mid] <= nums[end]:
            if target > nums[mid] and target <= nums[end]:
                return self.search(nums, target, mid+1, end)
            else:
                return self.search(nums, target, start, mid-1)