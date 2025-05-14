class Solution:
    def getAttachedLand(self, grid, i, j, m, n):
        if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == "1":
            grid[i][j] = "0"
        else:
            return
        self.getAttachedLand(grid, i+1, j, m, n)
        self.getAttachedLand(grid, i, j+1, m, n)
        self.getAttachedLand(grid, i-1, j, m, n)
        self.getAttachedLand(grid, i, j-1, m, n)


    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.getAttachedLand(grid, i, j, m, n)
                    islands+=1
        return islands
