class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0
        if left == right:
            return left
        ans = left
        def getBits(n):
            bits = ''
            while n > 0:
                bits+=str(n%2)
                n = n//2
            return bits
        leftBits = getBits(left)
        rightBits = getBits(right)
        if len(leftBits) != len(rightBits):
            return 0
        n = len(leftBits)
        diff_bits = len(getBits(right-left))
        ans = 0
        for i in range(n-1, -1, -1):
            if leftBits[i] != rightBits[i]:
                break
            if leftBits[i] == '1':
                ans += 2**i
        return ans
