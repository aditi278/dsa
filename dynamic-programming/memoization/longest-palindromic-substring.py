class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        n = len(s)
        if n < 2:
            return s
        memo = [['']*n for _ in range(n)]
        def checkPalindrome(i, j, memo):
            ini, inj = i, j
            while j > i:
                if memo[i][j] != '':
                    return memo[i][j], memo
                if s[i] != s[j]:
                    memo[ini][inj] = "$"
                    memo[i][j] = "$"
                    return "$", memo
                i+=1
                j-=1
            i, j = ini, inj
            while j > i:
                memo[i][j] = s[i:j+1]
                i+=1
                j-=1
            memo[ini][inj] = s[ini:inj+1]
            return s[ini:inj+1], memo
        
        
        for i in range(n):
            for j in range(i+1, n):
                curr, memo = checkPalindrome(i, j, memo)
                if len(curr) > len(longest):
                    longest = curr
        return longest