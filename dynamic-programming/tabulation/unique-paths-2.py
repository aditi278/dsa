class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "#"
        for i in range(m):
            if obstacleGrid[i][0] == "#":
                break
            obstacleGrid[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == "#":
                break
            obstacleGrid[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != "#":
                    if obstacleGrid[i-1][j] != "#":
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if obstacleGrid[i][j-1] != "#":
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1] if obstacleGrid[m-1][n-1] != "#" else 0