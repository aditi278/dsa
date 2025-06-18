class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        i = 0
        arr = []
        while i < len(nums):
            tmp = []
            for j in range(3):
                tmp.append(nums[i])
                if nums[i] - tmp[0] > k:
                    return []
                i += 1
            arr.append(tmp)
        return arr