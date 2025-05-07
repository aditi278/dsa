class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            while n-count-1>=0 and nums[n-count-1] == val:
                    #print(i, n-count-1)
                    count+=1
            if nums[i] == val and i<n-count:
                nums[i], nums[n-count-1]= nums[n-count-1], nums[i]
                count+=1
                #print(count)
        return n-count
