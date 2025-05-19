class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        totalSum = 0
        minSum = nums[0]
        firstMax = None
        currMax = 0
        currMin = 0
        for x in nums:
            currMax = max(currMax+x, x)
            currMin = min(currMin+x, x)
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
            totalSum +=x
        if totalSum == minSum:
            return maxSum
        return max(maxSum, totalSum - minSum)
   