class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        tmp = n
        n = abs(n)
        ans = 1
        rem = 0
        while n:
            if n%2:
                ans*=x
            x*=x
            n = n//2
        
        if tmp < 0:
            return 1/ans
        return ans