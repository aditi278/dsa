class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        m = {}
        for i in range(numRows):
            m[i] = ''
        parse = 'u-to-d'
        j = 0
        for i in range(len(s)):
            m[j]+=s[i]
            if j == 0:
                parse = 'u-to-d'
            elif j == numRows-1:
                parse = 'd-t0-u'
            if parse == 'u-to-d':
                j+=1
            else:
                j-=1
        
        zigzag=''
        for i in range(numRows):
            zigzag+=m[i]
        return zigzag