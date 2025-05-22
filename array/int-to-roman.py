class Solution:
    def roman(self, num, divisor, s, char):
        n = num//divisor
        for i in range(n):
            s+=char
        return num%divisor, s
    
    def intToRoman(self, num: int) -> str:
        s = ''
        num, s = self.roman(num, 1000, s, 'M')
        num, s = self.roman(num, 900, s, 'CM')
        num, s = self.roman(num, 500, s, 'D')
        num, s = self.roman(num, 400, s, 'CD')
        num, s = self.roman(num, 100, s, 'C')
        num, s = self.roman(num, 90, s, 'XC')
        num, s = self.roman(num, 50, s, 'L')
        num, s = self.roman(num, 40, s, 'XL')
        num, s = self.roman(num, 10, s, 'X')
        num, s = self.roman(num, 9, s, 'IX')
        num, s = self.roman(num, 5, s, 'V')
        num, s = self.roman(num, 4, s, 'IV')
        num, s = self.roman(num, 1, s, 'I')
        return s
