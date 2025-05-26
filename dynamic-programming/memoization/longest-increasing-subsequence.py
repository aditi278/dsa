class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        def getMemo(memo, i):
            if i > len(nums)-1:
                #print("len i", i)
                memo[len(nums)-1] = 1
                return 0
            if i == len(nums)-1:
                #print("len i", i)
                memo[len(nums)-1] = 1
                return 1
            if memo[i] > 0:
                #print("memo i", i, memo[i])
                return memo[i]
            #currMax = self.lengthOfLIS(nums, memo, i+1)
            currMax = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    currMax = max(currMax, 1 + getMemo(memo, j))
                    #print(i, j, nums[i], nums[j], memo[j])
            memo[i] = currMax
            #print(i, nums[i], memo)
            return memo[i]
        
        for i in range(len(memo)):
            if memo[i] == 0:
                getMemo(memo, i)
        
        return max(memo)