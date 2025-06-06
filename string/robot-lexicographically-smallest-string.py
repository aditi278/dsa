import collections
class Solution:
    def robotWithString(self, s: str) -> str:
        m = collections.defaultdict(int)
        i = 0
        t = []
        paper = ''
        for x in s:
            m[x] += 1
        
        def helper(m):
            for i in range(26):
                ch = chr(ord('a')+i)
                print(ch, m[ch])
                if m[ch] > 0:
                    return ch
            return 'a'


        for x in s:
            t.append(x)
            m[x]-=1
            while len(t)>0 and t[-1] <= helper(m):
                i+=1
                paper+=t.pop()
        return paper+''.join(t[::-1])