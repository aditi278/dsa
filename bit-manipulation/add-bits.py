class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = '0'
        n = len(a) - 1
        m = len(b) - 1
        bsum = ''
        while n >= 0 and m >= 0:
            
            if a[n] == '1' and b[m] == '1':
                if c == '1':
                    bsum+='1'
                else:
                    bsum+='0'
                    c = '1'
            elif a[n] == '0' and b[m] == '0':
                if c == '1':
                    bsum+='1'
                    c = '0'
                else:
                    bsum+='0'
            else:
                if c == '1':
                    bsum+='0'
                else:
                    bsum+='1'
            m-=1
            n-=1
        
        while m >= 0:
            if b[m] == '1':
                if c == '1':
                    bsum+='0'
                else:
                    bsum+='1'

            if b[m] == '0':
                if c == '1':
                    bsum+='1'
                    c = '0'
                else:
                    bsum+='0'
            m-=1
        while n >= 0:
            if a[n] == '1':
                if c == '1':
                    bsum+='0'
                else:
                    bsum+='1'

            if a[n] == '0':
                if c == '1':
                    bsum+='1'
                    c = '0'
                else:
                    bsum+='0'
            n-=1
        if c == '1':
            bsum+='1'
        return bsum[::-1]
        