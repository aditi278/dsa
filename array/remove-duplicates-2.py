class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n-1]
        count = 0
        dup_count = 0
        while n>0:
            if nums[n-1] == last:
                dup_count+=1
                if dup_count>2:
                    nums.pop(n-1)
                else:
                    count+=1
            else:
                count+=1
                dup_count=1
                last = nums[n-1]
            n-=1
        
        return count