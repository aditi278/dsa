class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        for i in range(len(s)):
            if s[i] not in m.keys() and t[i] not in m.values():
                m[s[i]]=t[i]
            elif s[i] not in m.keys() or m[s[i]] != t[i]:
                return False

        return True