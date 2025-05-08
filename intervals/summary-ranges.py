class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        l = []
        last = nums[0]
        start = nums[0]
        for x in nums:
            if x > last+1:
                if start == last:
                    l.append(str(last))
                else:
                    l.append(str(start)+'->'+str(last))
                start = x
            last=x
        if start == last:
            l.append(str(last))
        else:
            l.append(str(start)+'->'+str(last))
        return l
