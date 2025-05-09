class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            l = []
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in l:
                        return False
                    l.append(board[i][j])
        for i in range(9):
            l = []
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in l:
                        return False
                    l.append(board[j][i])
        r = 0
        while r < 9:
            c = 0
            while c < 9:
                l = []
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j] != '.':
                            if board[i][j] in l:
                                return False
                            l.append(board[i][j])
                c+=3
            r+=3
        return True