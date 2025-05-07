class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1
        while s[i] == ' ':
            i-=1
        end = i
        while i>=0 and s[i] != ' ':
            i-=1
        return end - i