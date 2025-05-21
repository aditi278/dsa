class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        i = 1
        while i < len(points):
            if points[i][0] <= points[i-1][1]:
                points[i-1][1] = min(points[i-1][1], points[i][1])
                points.pop(i)
                i-=1
            i+=1
        print(points)
        return len(points)