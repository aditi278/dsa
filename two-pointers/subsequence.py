class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(t) == 0 and len(s) == 0:
            return True
        for x in s:
            while i<len(t) and t[i] != x:
                i += 1
            i+=1
        if i > len(t):
            return False
        return True
        