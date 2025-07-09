class Solution:
    def reverse(self, x: int) -> int:
        n = 1
        if x < 0:
            n = -1
        
        x = abs(x)
        while x % 10 == 0 and x > 0:
            x = x//10
        num = x%10
        x = x//10
        while x > 0:
            if num*10 > 2**31 + 1:
                return 0
            num *= 10
            num += x%10
            x = x//10
        
        return num*n