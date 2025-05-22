class Solution:
    def permute(self, nums: List[int], arr=None, li=None) -> List[List[int]]:
        if arr is None:
            arr = []
        if li is None:
            li = []
        if len(li) == len(nums):
            tmp = [x for x in li]
            arr.append(tmp)
            return arr
        for x in nums:
            if x not in li:
                li.append(x)
                self.permute(nums, arr, li)
                li.pop()
        return arr