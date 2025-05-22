class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums[n-1] = True
        for i in range(n-2, -1, -1):
            if i + nums[i] >= n-1 or nums[i+nums[i]]:
                count = i+1
                tmp = nums[i]
                nums[i] = True
                while count <= i + tmp and count < n-1:
                    if nums[count]:
                        break
                    nums[count] = True
                    count+=1
            else:
                nums[i] = False
        return nums[0]
        