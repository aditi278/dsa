class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo=None) -> bool:
        if memo is None:
            memo = {}
        if s in wordDict:
            memo[s] = True
            return memo[s]
        res = False
        if s in memo:
            return memo[s]
        for word in wordDict:
            if s.startswith(word) and s not in memo:
                res = res or self.wordBreak(s[len(word):], wordDict, memo)
        memo[s] = res
        return memo[s]