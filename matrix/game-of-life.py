class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        pastRow = [0]*n   
        for i in range(m):
            pastNum = 0
            tmp = [x for x in board[i]]
            for j in range(n):
                count = 0
                count+=pastRow[j]
                count+=pastNum
                if j>0:
                    count+=pastRow[j-1]
                    if i < m-1:
                        count+=board[i+1][j-1]
                if j<n-1:
                    count+=pastRow[j+1]
                    count+=board[i][j+1]
                    if i < m-1:
                        count+=board[i+1][j+1]
                if i < m-1:
                    count+=board[i+1][j]
                pastNum = board[i][j]
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                elif count == 3:
                    board[i][j] = 1
            pastRow = tmp
