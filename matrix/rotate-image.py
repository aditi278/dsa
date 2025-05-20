class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        b = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                b[i][j] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = b[n - 1 - j][i]