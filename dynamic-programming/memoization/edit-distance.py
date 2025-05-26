class Solution:
    def minDistance(self, word1: str, word2: str, memo=None) -> int:
        if memo is None:
            memo = {}
        if word1 == word2:
            return 0
        if word1 == '' or word2 == '':
            memo[tuple([word1, word2])] = max(len(word1), len(word2))
            return memo[tuple([word1, word2])]
        if tuple([word1, word2]) in memo:
            return memo[tuple([word1, word2])]
        if tuple([word2, word1]) in memo:
            return memo[tuple([word2, word1])]
        currMin = 1 + min(self.minDistance(word1[1:], word2[1:], memo), self.minDistance(word1[1:], word2, memo), self.minDistance(word1, word2[1:], memo))
        if word1[0] == word2[0]:
            currMin = min(currMin, self.minDistance(word1[1:], word2[1:], memo))
        memo[tuple([word1, word2])] = currMin
        return memo[tuple([word1, word2])]