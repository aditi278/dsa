class Solution:
    def searchRange(self, nums: List[int], target: int, start=0, end=None, arr=None) -> List[int]:
        if end is None:
            end = len(nums) - 1
            arr = [-1, -1]
        if end < start:
            return arr
        mid = (start+end)//2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                arr[0] = mid
            else:
                self.searchRange(nums, target, start, mid-1, arr)
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                arr[1] = mid
            else:
                self.searchRange(nums, target, mid+1, end, arr)
        elif target < nums[mid]:
            self.searchRange(nums, target, start, mid-1, arr)
        elif target > nums[mid]:
            self.searchRange(nums, target, mid + 1, end, arr)
        return arr