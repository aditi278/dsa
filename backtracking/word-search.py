class Solution:
    def exist(self, board: List[List[str]], word: str, i=0, j=0) -> bool:
        m = len(board)
        n = len(board[0])
        def search(i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = 0
            found = search(i-1, j, word[1:]) or search(i+1, j, word[1:]) or search(i, j-1, word[1:]) or search(i, j+1, word[1:])
            board[i][j] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if search(i, j, word):
                    return True
        return False