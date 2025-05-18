class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def change(board, i, j, li=None):
            if li is None:
                li = []
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                return False
            board[i][j] = "X"
            chg = True
            if board[i][j-1] == "O":
                chg = chg and change(board, i, j-1, li)
            if board[i][j+1] == "O":
                chg = chg and change(board, i, j+1, li)
            if board[i+1][j] == "O":
                chg = chg and change(board, i+1, j, li)
            if board[i-1][j] == "O":
                chg = chg and change(board, i-1, j, li)
            if not chg:
                board[i][j] = "O"
                for x in li:
                    board[x[0]][x[1]] = "O"
            else:
                li.append([i,j])

            return chg
            

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    change(board, i, j)