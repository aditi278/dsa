class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        last = ''
        num=0
        for i in range(n):
            rom = s[n-1-i]
            if rom == 'I':
                if last == 'V' or last == 'X':
                    num-=1
                else:
                    num+=1
            elif rom == 'V':
                num+=5
            elif rom == 'X':
                if last == 'L' or last == 'C':
                    num-=10
                else:
                    num+=10
            elif rom == 'L':
                num+=50
            elif rom == 'C':
                if last == 'D' or last == 'M':
                    num-=100
                else:
                    num+=100
            elif rom == 'D':
                num+=500
            elif rom == 'M':
                num+=1000
            last = rom
        return num

        