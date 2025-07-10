class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        n = 1
        if len(s) < 1:
            return 0
        if s[0] == '-':
            n = -1
            s = s[1:]
        if len(s) < 1:
            return 0
        
        p = 0
        while s[0] == '0':
            p = 1
            s = s[1:]
            if len(s) < 1:
                return 0
        
        num = 0
        for x in s:
            if x.isdigit():
                p = 1
                num *= 10
                num += int(x)
            elif x == "+" and n > 0 and p == 0:
                p = 1
                continue
            else:
                break


        if n < 0:
            return num*n if num < 2**31 else n*(2**31)
        else:
            return num if num < 2**31 else 2**31 - 1