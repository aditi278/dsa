class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while n > 0:
            zeroes+=n//5
            n=n//5

        return zeroes