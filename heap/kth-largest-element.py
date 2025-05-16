import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = 0-nums[i]

        heapq.heapify(nums)
        x=0
        while k>0:
            x = heapq.heappop(nums)
            k-=1
        return 0 - x
