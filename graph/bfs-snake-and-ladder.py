class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(ceil(n/2)):
            board[i], board[n-i-1] = board[n-i-1], board[i]
        for i in range(n):
            if i % 2:
                board[i] = board[i][::-1]
          
        q = deque()
        q.append((1,0))
        s = set()
        while q:
            square, moves = q.popleft()
            for x in range(1, 7):
                next_square = square + x
                i = (next_square-1)//n
                j = (next_square-1)%n
                if board[i][j] != -1:
                    next_square = board[i][j]
                if next_square == n*n:
                    return moves + 1
                if next_square > n*n:
                    break
                if next_square not in s:
                    s.add(next_square)
                    q.append((next_square, moves+1))
        return -1