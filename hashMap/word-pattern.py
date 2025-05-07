class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(' ')
        if len(pattern) != len(strs):
            return False
        m = {}
        for i in range(len(pattern)):
            if pattern[i] not in m.keys():
                m[pattern[i]] = strs[i]
            elif m[pattern[i]] != strs[i]:
                return False
        m = {}
        for i in range(len(strs)):
            if strs[i] not in m.keys():
                m[strs[i]] = pattern[i]
            elif m[strs[i]] != pattern[i]:
                return False
        return True