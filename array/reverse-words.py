class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        s = ''
        for x in l[::-1]:
            if x != '':
                s += x
                s += ' '
        return s.strip()