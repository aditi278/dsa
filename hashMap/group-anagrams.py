class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in m.keys():
                m[temp] = [s]
            else:
                t = m[temp]
                t.append(s)
                m[temp] = t
        out = []
        for v in m.values():
            out.append(v)
        return out