class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        new_intervals = []
        inserted = False
        while i < len(intervals):
            if newInterval[0] <= intervals[i][0]:
                if intervals[i][0] <= newInterval[1]:
                    newInterval = [newInterval[0], max(newInterval[1], intervals[i][1])]
                    i+=1
                else:
                    new_intervals.append(newInterval)
                    inserted = True
                    break
                
            elif newInterval[0] <= intervals[i][1]:
                newInterval = [intervals[i][0], max(newInterval[1], intervals[i][1])]
                i+=1
            else:   
                new_intervals.append(intervals[i])
                i+=1
        if not inserted:
            new_intervals.append(newInterval)
        while i < len(intervals):
            new_intervals.append(intervals[i])
            i+=1
        return new_intervals