class Solution:
    def isHappy(self, n: int) -> bool:
        m = [n]
        while True:
            s=0
            for x in str(n):
                s+=int(x)*int(x)
            if s == 1:
                return True
            elif s in m:
                return False
            else:
                m.append(s)
                n=s
