class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)-1
        intervals.sort()
        i = 0
        while i<n:
            print(i)
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)
                i-=1
                n-=1
            i+=1
        return intervals