import collections
import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        m = collections.defaultdict(deque)
        
        removals = [True]*len(s)
        ans = ''
        
        def findMin(m):
            for i in range(26):
                ch = chr(ord('a') + i)
                if m[ch]:
                    return ch
            return 'z'

        min_char = []

        
        for i in range(len(s)):
            if s[i] == '*':
                removals[i] = False
                removals[m[heapq.heappop(min_char)].pop()] = False
                
            else:
                m[s[i]].append(i)
                heapq.heappush(min_char, s[i])
            
        
        for i in range(len(s)):
            if removals[i]:
                ans+=s[i]

        return ans