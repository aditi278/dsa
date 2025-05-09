class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n > 0:
            if n%2 == 1:
                set_bits+=1
            n = n//2
        return set_bits