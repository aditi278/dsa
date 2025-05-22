class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        prod = 1
        for x in nums:
            if x:
                prod*=x
            else:
                count += 1
        n = len(nums)
        arr = [0]*n
        if count > 1:
            return arr
        elif count == 1:
            for i in range(n):
                if nums[i] == 0:
                    arr[i] = prod
                    return arr
        for i in range(n):
            arr[i] = int(prod/nums[i])
        return arr