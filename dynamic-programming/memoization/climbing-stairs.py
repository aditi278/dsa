class Solution:
    def climbStairs(self, n: int, memo=None) -> int:
        if memo is None:
            memo = [0]*n
        if n == 1:
            memo[n-1] = 1
        if n == 2:
            memo[n-1] = 2
        
        if memo[n-1] == 0:
            memo[n-1] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n-1]
      