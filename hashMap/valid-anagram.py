class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in range(len(s)):
            if s[i] not in m.keys():
                m[s[i]] = 1
            else:
                m[s[i]] += 1
            if t[i] not in m.keys():
                m[t[i]] = -1
            else:
                m[t[i]] -= 1
        for _, val in m.items():
            if val != 0:
                return False
        return True
