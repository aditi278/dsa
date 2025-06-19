class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr = []
        tmp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - tmp[0] > k:
                arr.append(tmp)
                tmp = []
            tmp.append(nums[i])
        if tmp:
            arr.append(tmp)
        return len(arr)