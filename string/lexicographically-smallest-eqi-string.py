import collections

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        edges = collections.defaultdict(set)
        for i in range(len(s1)):
            edges[s1[i]].add(s1[i])
            edges[s1[i]].add(s2[i])
            edges[s2[i]].add(s1[i])
            edges[s2[i]].add(s2[i])
        
        m = {}
        newStr = ''
        for i in range(len(baseStr)):
            if baseStr[i] in m:
                newStr += m[baseStr[i]]
                continue
            visited = set()
            q = deque()
            q.append(baseStr[i])
            min_char = baseStr[i]
            while q:
                char = q.popleft()
                if char not in visited and char in edges:
                    visited.add(char)
                    for x in edges[char]:
                        min_char = min(min_char, x)
                        q.append(x)
            for x in visited:
                m[x] = min_char
            newStr += min_char
            
        return newStr