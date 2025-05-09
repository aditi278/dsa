class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            x = (digits[-(i+1)]+carry)
            carry = x//10
            digits[-(i+1)]= x%10
            if not carry:
                break
        if carry:
            digits.insert(0,1)
        return digits
        