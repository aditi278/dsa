class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        l = len(haystack)
        i = 0
        while l-i>=n:
            if haystack[i:].startswith(needle):
                return i
            i+=1
        return -1